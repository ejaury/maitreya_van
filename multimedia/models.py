import os
import zipfile

try:
    import Image
except ImportError:
    from PIL import Image

from django.core.files.base import ContentFile
from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import ugettext_lazy as _

from photologue.models import Gallery, Photo as OriginalPhoto
from photologue.models import PHOTOLOGUE_DIR, tagfield_help_text

from maitreya_van.general.models import Category
from maitreya_van.utils.managers import PluggableQuerySetManager
from tagging.fields import TagField


class EmbeddedVideo(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True,
        help_text='A "slug" is a unique URL-friendly title \
                  (link name) for an object. (e.g. category Community \
                  Performance can have a slug named "comm-performance",\
                  in which the pages can be accessed via \
                  http://www.mywebsite.com/category/comm-performance')
    link = models.CharField(max_length=512, blank=True, help_text=_('Only a Youtube link is allowed here'))
    embed_code = models.TextField(blank=True, help_text=_('If you have the actual embed code, you can directly copy and paste it here without specifying a link. To obtain an embed code from Youtube, under the video, click on "Share" button, then click on "Embed", to show the code. Paste the code in the above field. It would be better if you specify an embed code rather than a link because this way you can embed a video from any site (not only Youtube).'))
    description = models.TextField(blank=True)
    timestamp = models.DateTimeField(verbose_name=_('date published'),
        auto_now_add=True, null=True)
    tags = TagField(help_text='Separate tags with spaces, put quotes around \
                    multiple-word tags.',
                    verbose_name=('tags'))
    categories = models.ManyToManyField(Category, limit_choices_to = {
                'content_type__model': 'EmbeddedVideo',
               }, blank=True)

    class Meta:
        verbose_name = _('video')
        ordering = ('-timestamp',)

    def __unicode__(self):
        return self.title


class MusicQuerySet(models.query.QuerySet):
    """Queryset for Music model to remove associated uploaded files"""
    def delete(self):
        # Delete assoaciated files first
        for music in self:
            try:
                music.file.delete()
            except Exception:
                pass
        super(MusicQuerySet, self).delete()


class Music(models.Model):
    file = models.FileField(upload_to='music')
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=50, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, null=True)
    tags = TagField(help_text='Separate tags with spaces, put quotes around \
                    multiple-word tags.',
                    verbose_name=('tags'))

    objects = PluggableQuerySetManager(MusicQuerySet)
    
    class Meta:
        get_latest_by = 'timestamp'
        verbose_name_plural = _('music')

    @property
    def song_title(self):
        if self.artist:
            return '%s - %s' % (self.artist, self.title)
        return self.title

    def __unicode__(self):
        return self.song_title

    def delete(self, *args, **kwargs):
        try:
            self.file.delete()
        except Exception:
            pass
        super(Music, self).delete(*args, **kwargs)


class PhotoGallery(Gallery):
    categories = models.ManyToManyField(Category, limit_choices_to = {
                'content_type__model': 'PhotoGallery',
               }, blank=True)

    class Meta:
        verbose_name_plural = 'Photo Galleries'


class PhotoGalleryUpload(models.Model):
    """
    Model that's simply used to upload photos in batch.
    Copied directly from photologue's GalleryUpload.
    """
    zip_file = models.FileField(_('images file (.zip)'), upload_to=PHOTOLOGUE_DIR+"/temp",
                                help_text=_('Select a .zip file of images to upload into a new Gallery.'))
    gallery = models.ForeignKey(PhotoGallery, null=True, blank=True, help_text=_('Select a gallery to add these images to. leave this empty to create a new gallery from the supplied title.'))
    title = models.CharField(_('title'), max_length=75, help_text=_('All photos in the gallery will be given a title made up of the gallery title + a sequential number.'))
    caption = models.TextField(_('caption'), blank=True, help_text=_('Caption will be added to all photos.'))
    description = models.TextField(_('description'), blank=True, help_text=_('A description of this Gallery.'))
    is_public = models.BooleanField(_('is public'), default=True, help_text=_('Uncheck this to make the uploaded gallery and included photographs private.'))
    tags = TagField(help_text=tagfield_help_text, verbose_name=_('tags'))

    class Meta:
        verbose_name = _('photo gallery upload')

    def save(self, *args, **kwargs):
        super(PhotoGalleryUpload, self).save(*args, **kwargs)
        gallery = self.process_zipfile()
        super(PhotoGalleryUpload, self).delete()
        return gallery

    def process_zipfile(self):
        if os.path.isfile(self.zip_file.path):
            # TODO: implement try-except here
            zip = zipfile.ZipFile(self.zip_file.path)
            bad_file = zip.testzip()
            if bad_file:
                raise Exception('"%s" in the .zip archive is corrupt.' % bad_file)
            count = 1
            if self.gallery:
                gallery = self.gallery
            else:
                gallery = PhotoGallery.objects.create(title=self.title,
                                                      title_slug=slugify(self.title),
                                                      description=self.description,
                                                      is_public=self.is_public,
                                                      tags=self.tags)
            from cStringIO import StringIO
            for filename in zip.namelist():
                if filename.startswith('__'): # do not process meta files
                    continue
                data = zip.read(filename)
                if len(data):
                    try:
                        # the following is taken from django.newforms.fields.ImageField:
                        #  load() is the only method that can spot a truncated JPEG,
                        #  but it cannot be called sanely after verify()
                        trial_image = Image.open(StringIO(data))
                        trial_image.load()
                        # verify() is the only method that can spot a corrupt PNG,
                        #  but it must be called immediately after the constructor
                        trial_image = Image.open(StringIO(data))
                        trial_image.verify()
                    except Exception:
                        # if a "bad" file is found we just skip it.
                        continue
                    while 1:
                        title = ' '.join([self.title, str(count)])
                        slug = slugify(title)
                        try:
                            p = Photo.objects.get(title_slug=slug)
                        except Photo.DoesNotExist:
                            photo = Photo(title=title,
                                          title_slug=slug,
                                          caption=self.caption,
                                          is_public=self.is_public,
                                          tags=self.tags)
                            photo.image.save(filename, ContentFile(data))
                            gallery.photos.add(photo)
                            count = count + 1
                            break
                        count = count + 1
            zip.close()
            return gallery


class Photo(OriginalPhoto):
    """Act as a proxy model to the real Photo model from photologue. We do this
    so that we can re-group this model with Multimedia app."""
    class Meta:
        proxy = True
