import datetime
import random

from django.conf import settings
from django.shortcuts import render_to_response
from django.template import RequestContext

from maitreya_van.schedule.models import Event, Calendar
from maitreya_van.schedule.periods import Period

from photologue.models import Photo
from PIL import Image

def index(request):
    event_limit = int(getattr(settings, 'UPCOMING_EVENTS_LIMIT', 3))
    default_cal = getattr(settings, 'DEFAULT_CALENDAR_SLUG')
    calendar = Calendar.objects.get(slug=default_cal)
    events = Event.objects.filter(calendar=calendar)
    start = datetime.datetime.now()
    end = start + datetime.timedelta(days=365)
    occurrences = Period(events, start, end).get_occurrences()[:event_limit]

    # Get random photos
    photo_count = Photo.objects.count()

    if photo_count >= settings.MIN_SLIDESHOW_PHOTOS:
        # Materialize queryset
        photos = list(Photo.objects.all()[0:photo_count])
        photo_urls = []

        while len(photo_urls) < settings.MIN_SLIDESHOW_PHOTOS:
            idx = random.randint(0, photo_count - 1)
            p = photos[idx]
            if p.image.url not in photo_urls:
                im = Image.open(p.image.path)
                width, height = im.size
                if width/height > 0:
                    photo_urls.append(p.image.url)

    return render_to_response('main/index.html', {
        'occurrences': occurrences,
        'photo_urls': photo_urls,
    }, context_instance=RequestContext(request))
