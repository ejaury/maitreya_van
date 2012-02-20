from django.db import models
from django.utils.translation import ugettext_lazy as _

from maitreya_van.general.models import Category, TaggablePage

from tagging.fields import TagField


class About(TaggablePage):
    class Meta:
        verbose_name = _('about us')
        verbose_name_plural = verbose_name

    @models.permalink
    def get_absolute_url(self):
        return ('about_page_detail', (), {
            'pk': self.id,
            'slug': self.slug,
        })


class Maitreya(TaggablePage):
    categories = models.ManyToManyField(Category, blank=True, null=True,
        limit_choices_to = {'content_type__model': 'Maitreya'})

    class Meta:
        verbose_name = _('Maitreya Buddha')
        verbose_name_plural = verbose_name

    @models.permalink
    def get_absolute_url(self):
        return ('maitreya_detail', (), {
            'pk': self.id,
            'slug': self.slug,
        })


class PastEvent(TaggablePage):
    @models.permalink
    def get_absolute_url(self):
        return ('past_event_detail', (), {
            'pk': self.id,
            'slug': self.slug,
        })


class Story(TaggablePage):
    categories = models.ManyToManyField(Category, blank=True, null=True,
        limit_choices_to={'content_type__model': 'Story'})

    class Meta:
        verbose_name_plural = 'Stories'

    @models.permalink
    def get_absolute_url(self):
        return ('story_detail', (), {
            'pk': self.id,
            'slug': self.slug,
        })


class News(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True, auto_now=True)
    tags = TagField(verbose_name=('tags'), help_text='Separate tags with spaces, \
        put quotes around multiple-word tags.')

    class Meta:
        ordering = ('-pub_date',)
        verbose_name_plural = _('news')

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('news_detail', (), {
            'pk': self.id,
            'slug': self.slug,
        })
