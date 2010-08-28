from django.db import models
from django.template.defaultfilters import slugify
from maitreya_van.general.models import Category, TaggablePage

class Class(TaggablePage):
  categories = models.ManyToManyField(Category, limit_choices_to = {
                'content_type__model': 'Class',
               })
  
  class Meta:
    verbose_name_plural = 'Classes'

  @models.permalink
  def get_absolute_url(self):
    return ('maitreya_van.classes.views.view_page', (), {
              'class_id': self.id,
              'slug': slugify(self.title),
            })
