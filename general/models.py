import datetime
import logging

from django.contrib.contenttypes.models import ContentType
from django.contrib.sitemaps import ping_google
from django.db import models
from django.utils.encoding import force_unicode
from exceptions import NotImplementedError
from maitreya_van.navigation.models import MenuItemExtension
from tagging.fields import TagField
from treemenus.models import MenuItem

logger = logging.getLogger(__name__)


class BasePage(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True,
        help_text='A "slug" is a unique URL-friendly title \
                  (link name) for an object. (e.g. category Community \
                  Performance can have a slug named "comm-performance",\
                  in which the pages can be accessed via \
                  http://www.mywebsite.com/pages/comm-performance')
    content = models.TextField()
    menu_item = models.OneToOneField(MenuItem, null=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True,
        default=datetime.datetime.today())
    updated_at = models.DateTimeField(auto_now=True,
        default=datetime.datetime.today())

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.title

    def delete(self, *args, **kwargs):
        if self.menu_item:
            try:
                menu_ext = MenuItemExtension.objects.get(menu_item=self.menu_item)
                menu_ext.delete()
            except MenuItemExtension.DoesNotExist:
                pass
            self.menu_item.delete()
        super(BasePage, self).delete(*args, **kwargs)

    def save(self, *args, **kwargs):
        super(BasePage, self).save(*args, **kwargs)
        try:
            ping_google()
        except:
            logger.exception('Error informing Google about a new entry in "%(model)s" page: %(title)s' % {
                'model': force_unicode(self._meta.verbose_name),
                'title': self.title,
            })

    @models.permalink
    def get_absolute_url(self):
        raise NotImplementedError


class TaggablePage(BasePage):
    tags = TagField(help_text='Separate tags with spaces, put quotes around \
                    multiple-word tags.',
                    verbose_name=('tags'))

    class Meta:
        abstract = True


class Category(models.Model):
    content_type = models.ForeignKey(ContentType)
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True,
        help_text='A "slug" is a unique URL-friendly title \
                  (link name) for an object. (e.g. category Community \
                  Performance can have a slug named "comm-performance",\
                  in which the pages can be accessed via \
                  http://www.mywebsite.com/category/comm-performance')

    def __unicode__(self):
        return '%s: %s' % (self.content_type.name, self.name)

    class Meta:
        ordering = ['content_type', 'name']
        verbose_name_plural = 'Categories'
