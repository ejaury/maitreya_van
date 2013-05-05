from django.contrib.sitemaps import GenericSitemap

from maitreya_van.multimedia.models import EmbeddedVideo
from maitreya_van.pages.models import *

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
    'video': GenericSitemap(video_maps, changefreq='weekly'),
}
