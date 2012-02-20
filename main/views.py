import datetime
import random

from django.conf import settings
from django.shortcuts import render_to_response
from django.template import RequestContext

from maitreya_van.pages.models import News
from maitreya_van.multimedia.utils import get_latest_media
from maitreya_van.schedule.models import Event, Calendar
from maitreya_van.schedule.periods import Period

from photologue.models import Photo
from PIL import Image

def index(request):
    content_limit = int(getattr(settings, 'WIDGET_CONTENT_LIMIT', 3))
    default_cal = getattr(settings, 'DEFAULT_CALENDAR_SLUG')
    calendar = Calendar.objects.get(slug=default_cal)
    events = Event.objects.filter(calendar=calendar)
    start = datetime.datetime.now()
    end = start + datetime.timedelta(days=365)
    occurrences = Period(events, start, end).get_occurrences()[:content_limit]

    # Get random pics
    photo_urls = get_random_photo_urls()

    latest_media = get_latest_media()

    # Populate latest news
    news = News.objects.all()[:content_limit]

    return render_to_response('main/index.html', {
        'occurrences': occurrences,
        'photo_urls': photo_urls,
        'news_list': news,
        'latest_media': latest_media,
    }, context_instance=RequestContext(request))

def get_random_photo_urls():
    total_photos = Photo.objects.count()
    if total_photos == 0:
        return []

    photo_urls = []
    count = min(settings.MIN_SLIDESHOW_PHOTOS, total_photos)

    # Materialize queryset
    photo_ids = list(Photo.objects.all().values_list('id', flat=True)[:50])

    while len(photo_urls) < count:
        rand = random.randint(0, total_photos - 1)
        try:
            idx = photo_ids.pop(rand)
        except IndexError:
            continue

        try:
            p = Photo.objects.get(pk=idx)
        except Photo.DoesNotExist:
            continue

        # Only show public pics
        if not p.is_public:
            continue

        if p.image.url not in photo_urls:
            im = Image.open(p.image.path)
            width, height = im.size
            if width/height > 0:
                photo_urls.append(p.image.url)

    return photo_urls
