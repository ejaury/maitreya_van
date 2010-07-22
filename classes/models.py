from django.db import models
from django.template.defaultfilters import slugify
from maitreya_van.main.models import BasePage

class Class(BasePage):
  pass
  
  class Meta:
    verbose_name_plural = 'Classes'

  def __unicode__(self):
    return self.title

  @models.permalink
  def get_absolute_url(self):
    return ('maitreya_van.classes.views.view_page', (), {
              'class_id': self.id,
              'slug': slugify(self.title),
            })
