from django.db import models
from django.template.defaultfilters import slugify
from maitreya_van.main.models import BasePage

class Event(BasePage):
  category = models.CharField(max_length=30)
  start_date = models.DateTimeField()
  end_date = models.DateTimeField()
  location = models.CharField(max_length=50)
  # TODO: in view, use address to automatically populate Google Map URL
  address = models.CharField(max_length=100)

  def __unicode__(self):
    return '%s (%s - %s)' % (self.title, self.start_date, self.end_date)

  @models.permalink
  def get_absolute_url(self):
    return ('maitreya_van.events.views.detail', (), {
              'event_id': self.id,
              'slug': slugify(self.title),
            })
