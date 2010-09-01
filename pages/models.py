from django.db import models
from django.template.defaultfilters import slugify
from maitreya_van.general.models import Category, TaggablePage

class Class(TaggablePage):
  categories = models.ManyToManyField(Category, blank=True, null=True,
                                      limit_choices_to = {
                'content_type__model': 'Class',
               })
  
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
                                      limit_choices_to = {
                'content_type__model': 'Teaching',
               })

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
