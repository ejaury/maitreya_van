from django.conf import settings
from django.conf.urls.defaults import *

from maitreya_van.multimedia.models import *
from maitreya_van.multimedia.views import VideoDetailView, VideoListView

# Number of random images from the gallery to display.
SAMPLE_SIZE = ":%s" % getattr(settings, 'GALLERY_SAMPLE_SIZE', 5)
THUMB_ROW_SIZE = "%i" % getattr(settings, 'THUMBNAIL_ROW_SIZE', 4)

# galleries
gallery_args = {
    'date_field': 'date_added',
    'allow_empty': True,
    'queryset': PhotoGallery.objects.filter(is_public=True),
    'extra_context':{
        'sample_size':SAMPLE_SIZE,
        'thumb_size':THUMB_ROW_SIZE,
    }
}
urlpatterns = patterns('django.views.generic.date_based',
    url(r'^photos/gallery/(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\w{1,2})/(?P<slug>[\-\d\w]+)/$', 'object_detail', {'date_field': 'date_added', 'slug_field': 'title_slug', 'queryset': PhotoGallery.objects.filter(is_public=True), 'extra_context':{'sample_size':SAMPLE_SIZE}}, name='pl-gallery-detail'),
    url(r'^photos/gallery/(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\w{1,2})/$', 'archive_day', gallery_args, name='pl-gallery-archive-day'),
    url(r'^photos/gallery/(?P<year>\d{4})/(?P<month>[a-z]{3})/$', 'archive_month', gallery_args, name='pl-gallery-archive-month'),
    url(r'^photos/gallery/(?P<year>\d{4})/$', 'archive_year', gallery_args, name='pl-gallery-archive-year'),
    url(r'^photos/gallery/?$', 'archive_index', gallery_args, name='pl-gallery-archive'),
)
urlpatterns += patterns('django.views.generic.list_detail',
    url(r'^photos/gallery/(?P<slug>[\-\d\w]+)/$', 'object_detail', {
        'slug_field': 'title_slug',
        'queryset': PhotoGallery.objects.filter(is_public=True),
        'extra_context': {
            'sample_size':SAMPLE_SIZE,
            'thumb_size': THUMB_ROW_SIZE
        }
    }, name='pl-gallery'),
    url(r'^photos/gallery/page/(?P<page>[0-9]+)/$', 'object_list', {
        'queryset': PhotoGallery.objects.filter(is_public=True),
        'allow_empty': True,
        'paginate_by': 5,
        'extra_context': {
            'sample_size':SAMPLE_SIZE,
            'thumb_size':THUMB_ROW_SIZE
        }
    }, name='pl-gallery-list'),
)

# photographs
photo_args = {
    'date_field': 'date_added',
    'allow_empty': True,
    'queryset': Photo.objects.filter(is_public=True)
}
urlpatterns += patterns('django.views.generic.date_based',
    url(r'^photos/photo/(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\w{1,2})/(?P<slug>[\-\d\w]+)/$', 'object_detail', {
        'date_field': 'date_added',
        'slug_field': 'title_slug',
        'queryset': Photo.objects.filter(is_public=True),
        'template_name': 'photologue/photo_detail.html',
    }, name='pl-photo-detail'),
    url(r'^photos/photo/(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\w{1,2})/$', 'archive_day',
        dict(photo_args.items() + {'template_name': 'photologue/photo_archive_day.html'}.items()),
        name='pl-photo-archive-day'),
    url(r'^photos/photo/(?P<year>\d{4})/(?P<month>[a-z]{3})/$', 'archive_month',
        dict(photo_args.items() + {'template_name': 'photologue/photo_archive_month.html'}.items()),
        name='pl-photo-archive-month'),
    url(r'^photos/photo/(?P<year>\d{4})/$', 'archive_year',
        dict(photo_args.items() + {'template_name': 'photologue/photo_archive_year.html'}.items()),
        name='pl-photo-archive-year'),
    url(r'^photos/photo/$', 'archive_index',
        dict(photo_args.items() + {'template_name': 'photologue/photo_archive.html'}.items()),
        name='pl-photo-archive'),
)
urlpatterns += patterns('django.views.generic.list_detail',
    url(r'^photos/photo/(?P<slug>[\-\d\w]+)/$', 'object_detail', {
        'slug_field': 'title_slug',
        'queryset': Photo.objects.filter(is_public=True),
        'template_name': 'photologue/photo_detail.html',
    }, name='pl-photo'),
    url(r'^photos/photo/page/(?P<page>[0-9]+)/$', 'object_list', {
        'queryset': Photo.objects.filter(is_public=True),
        'allow_empty': True,
        'paginate_by': 20,
        'template_name': 'photologue/photo_list.html',
    }, name='pl-photo-list'),
)

# Other multimedia views
urlpatterns += patterns('maitreya_van.multimedia.views',
    url(r'^videos/$',
        VideoListView.as_view(),
        name='video_index'),
    url(r'^videos/(?P<slug>[\-\d\w]+)/$',
        VideoDetailView.as_view(),
        name='video_detail'),
    url(r'^music/$',
        'music_gallery_view',
        name='music_index')
)
