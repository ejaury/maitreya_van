from django.db import models
from photologue.models import Gallery, GalleryUpload
from maitreya_van.general.models import Category
from maitreya_van.utils.managers import PluggableQuerySetManager
from tagging.fields import TagField


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
    tags = TagField(help_text='Separate tags with spaces, put quotes around \
                    multiple-word tags.',
                    verbose_name=('tags'))

    objects = PluggableQuerySetManager(MusicQuerySet)

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
               })

    class Meta:
        verbose_name_plural = 'Photo Galleries'


class PhotoGalleryUpload(GalleryUpload):
    pass
