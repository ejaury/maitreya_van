import datetime
from django.conf import settings
from django.shortcuts import render_to_response
from maitreya_van.schedule.models import Event

def index(request):
  event_limit = int(getattr(settings, 'UPCOMING_EVENTS_LIMIT', 3))
  events = Event.objects.filter(start__gt=datetime.datetime.today()).order_by('start',
    'title')[:event_limit]
  return render_to_response('main/index.html', {
      'events': events,
    })
