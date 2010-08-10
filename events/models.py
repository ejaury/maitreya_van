from django.db import models
from django.template.defaultfilters import slugify
from maitreya_van.main.models import BasePage
from maitreya_van.thirdparty.schedule.models.events import Event

class DetailEvent(Event):
  # TODO: many-to-many relation with Category model
  #category = models.CharField(max_length=30)
  location = models.CharField(max_length=50)
  # TODO: in view, use address to automatically populate Google Map URL
  address = models.CharField(max_length=100)

  def __unicode__(self):
    return '%s (%s - %s)' % (self.title, self.start, self.end)

  @models.permalink
  def get_absolute_url(self):
    return ('maitreya_van.events.views.detail', (), {
              'event_id': self.id,
              'slug': slugify(self.title),
            })
