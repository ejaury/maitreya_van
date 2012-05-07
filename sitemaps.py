from datetime import datetime, timedelta

from django.conf import settings
from django.contrib.sitemaps import GenericSitemap, Sitemap
from django.core.urlresolvers import reverse

from maitreya_van.multimedia.models import EmbeddedVideo
from maitreya_van.pages.models import *
from maitreya_van.schedule.models import Event

# General pages
# =============
about_maps = {
    'queryset': About.objects.all(),
    'date_field': 'updated_at',
}

maitreya_maps = {
    'queryset': Maitreya.objects.all(),
    'date_field': 'updated_at',
}

pastevent_maps = {
    'queryset': PastEvent.objects.all(),
    'date_field': 'updated_at',
}

story_maps = {
    'queryset': Story.objects.all(),
    'date_field': 'updated_at',
}

news_maps = {
    'queryset': News.objects.all(),
    'date_field': 'pub_date',
}

# Schedule
# ========
class OccurrenceSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.7

    def items(self):
        events = Event.objects.filter(calendar__slug=settings.DEFAULT_CALENDAR_SLUG)
        now = datetime.now()
        year_later = now + timedelta(days=365)
        occurrences = []
        for e in events:
            occurrences.extend(e.get_occurrences(start=now, end=year_later))
        return occurrences

    def location(self, occurrence):
        return reverse('occurrence_by_date', kwargs={
            'event_id': occurrence.event.id,
            'year': occurrence.start.year,
            'month': occurrence.start.month,
            'day': occurrence.start.day,
            'hour': occurrence.start.hour,
            'minute': occurrence.start.minute,
            'second': occurrence.start.second,
        })

    def lastmod(self, occurrence):
        return occurrence.event.created_on

# Multimedia
# ==========
video_maps = {
    'queryset': EmbeddedVideo.objects.all(),
    'date_field': 'timestamp',
}

sitemaps = {
    'about': GenericSitemap(about_maps, priority=0.8),
    'maitreya': GenericSitemap(maitreya_maps, priority=0.9),
    'pastevent': GenericSitemap(pastevent_maps),
    'story': GenericSitemap(story_maps),
    'news': GenericSitemap(news_maps, changefreq='weekly', priority=0.7),
    'event': OccurrenceSitemap(),
    'video': GenericSitemap(video_maps, changefreq='weekly'),
}
