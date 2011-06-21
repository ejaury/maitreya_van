from django.conf import settings
from django.conf.urls.defaults import *
from maitreya_van.pages.models import *
from maitreya_van.pages.views import ContactView, PageDetailView, PageListView
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
    (r'^about/contact/', include('contact_form.urls')),
    (r'^events/upcoming/', include('maitreya_van.schedule.urls')),
    (r'^multimedia/', include('maitreya_van.multimedia.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^tinymce/', include('maitreya_van.add_ons.tinymce.urls')),
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {
      'document_root': settings.MEDIA_ROOT, 'show_indexes': True
    }),
)

urlpatterns += patterns('',
    url(r'^about/location/$',
        ContactView.as_view(),
        name='about_location'),
    url(r'^about/(?P<pk>\d+)/(?P<slug>[\w-]+)/$',
        PageDetailView.as_view(model=About),
        name='about_page_detail'),
    url(r'^classes/(?P<pk>\d+)/(?P<slug>[\w-]+)/$',
        PageDetailView.as_view(model=Class),
        name='class_detail'),
    url(r'^events/news/(?P<pk>\d+)/(?P<slug>[\w-]+)/$',
        PageDetailView.as_view(model=News),
        name='news_detail'),
    url(r'^events/past/(?P<pk>\d+)/(?P<slug>[\w-]+)/$',
        PageDetailView.as_view(model=PastEvent),
        name='past_event_detail'),
    url(r'^teachings/(?P<pk>\d+)/(?P<slug>[\w-]+)/$',
        PageDetailView.as_view(model=Teaching),
        name='teaching_detail'),
)

urlpatterns += patterns('django.views.generic.list_detail',
    url(r'^about/$',
        PageListView.as_view(model=About),
        name='about_page_index'),
    url(r'^classes/$',
        PageListView.as_view(model=Class),
        name='class_index'),
    url(r'^teachings/$',
        PageListView.as_view(model=Teaching),
        name='teaching_index'),
    url(r'^events/news/$',
        PageListView.as_view(model=News),
        name='news_index'),
    url(r'^events/past/$',
        PageListView.as_view(model=PastEvent),
        name='past_event_index'),
)
