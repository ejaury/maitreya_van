import datetime
from django.conf import settings
from django.shortcuts import render_to_response
from maitreya_van.schedule.models import Event, Calendar
from maitreya_van.schedule.periods import Period

def index(request):
  event_limit = int(getattr(settings, 'UPCOMING_EVENTS_LIMIT', 3))
  default_cal = getattr(settings, 'DEFAULT_CALENDAR_SLUG')
  calendar = Calendar.objects.get(slug=default_cal)
  events = Event.objects.filter(calendar=calendar)
  start = datetime.datetime.now()
  end = start + datetime.timedelta(days=365)
  occurrences = Period(events, start, end).get_occurrences()[:event_limit]
  return render_to_response('main/index.html', {
      'occurrences': occurrences,
    })
