from django.conf.urls.defaults import *
from maitreya_van.pages.models import *
from photologue.models import Gallery, GalleryUpload

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

# Hide these models from Admin page
admin.site.unregister(Gallery)
admin.site.unregister(GalleryUpload)

urlpatterns = patterns('',
    # Example:
    # (r'^maitreya_van/', include('maitreya_van.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^$', 'maitreya_van.main.views.index'),
    (r'^about/', include('maitreya_van.about.urls')),
    (r'^events/upcoming/', include('maitreya_van.schedule.urls')),
    (r'^multimedia/photos/', include('maitreya_van.multimedia.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^tinymce/', include('maitreya_van.add_ons.tinymce.urls')),
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {
      'document_root': '/home/edwin/maitreya_van/assets/', 'show_indexes': True
    }),
)

urlpatterns += patterns('maitreya_van.pages.views',
    (r'^classes/(?P<class_id>\d+)/(?P<slug>[\w-]+)/$', 'view_class'),
    (r'^events/past/(?P<past_event_id>\d+)/(?P<slug>[\w-]+)/$', 'view_past_event'),
    (r'^teachings/(?P<teaching_id>\d+)/(?P<slug>[\w-]+)/$', 'view_teaching'),
)

urlpatterns += patterns('django.views.generic.list_detail',
    url(r'^teachings/$', 'object_list', name='teaching_index', kwargs={
      'queryset': Teaching.objects.all(),
      'template_name' :'pages/index.html',
      'extra_context': {
        'title': 'Teachings',
      },
    }),
    url(r'^classes/$', 'object_list', name='class_index', kwargs={
      'queryset': Class.objects.all(),
      'template_name' :'pages/index.html',
      'extra_context': {
        'title': 'Classes',
      },
    }),
    url(r'^events/past/$', 'object_list', name='past_event_index', kwargs={
      'queryset': PastEvent.objects.all(),
      'template_name' :'pages/index.html',
      'extra_context': {
        'title': 'Past Events',
      },
    }),
)
