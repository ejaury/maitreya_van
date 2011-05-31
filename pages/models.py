from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import ugettext_lazy as _

from maitreya_van.general.models import Category, TaggablePage

from tagging.fields import TagField


class Class(TaggablePage):
    categories = models.ManyToManyField(Category, blank=True, null=True,
        limit_choices_to={'content_type__model': 'Class'})

    class Meta:
        verbose_name_plural = 'Classes'

    @models.permalink
    def get_absolute_url(self):
        return ('maitreya_van.pages.views.view_class', (), {
            'class_id': self.id,
            'slug': slugify(self.title),
        })


class Teaching(TaggablePage):
    categories = models.ManyToManyField(Category, blank=True, null=True,
        limit_choices_to = {'content_type__model': 'Teaching'})

    @models.permalink
    def get_absolute_url(self):
        return ('maitreya_van.pages.views.view_teaching', (), {
            'teaching_id': self.id,
            'slug': slugify(self.title),
        })


class PastEvent(TaggablePage):
    @models.permalink
    def get_absolute_url(self):
        return ('maitreya_van.pages.views.view_past_event', (), {
            'past_event_id': self.id,
            'slug': slugify(self.title),
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
        return ('maitreya_van.pages.views.view_news', (), {
            'news_id': self.id,
            'slug': slugify(self.title),
        })
