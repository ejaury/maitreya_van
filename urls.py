from django.conf import settings
from django.conf.urls.defaults import *
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from maitreya_van.pages.models import *
from maitreya_van.pages.views import ContactView, PageDetailView, PageListView,\
                                     TemplateView
from maitreya_van.sitemaps import sitemaps

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the next line to enable the admin:
    url(r'^$',
        'maitreya_van.main.views.index',
        name='home'),
    (r'^about/contact/', include('contact_form.urls')),
    (r'^events/', include('maitreya_van.schedule.urls')),
    (r'^multimedia/', include('maitreya_van.multimedia.urls')),
    (r'^grappelli/', include('grappelli.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^tinymce/', include('maitreya_van.add_ons.tinymce.urls')),
    (r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
)

urlpatterns += patterns('',
    url(r'^about/location/$',
        ContactView.as_view(),
        name='about_location'),
    url(r'^about/us/$',
        TemplateView.as_view(template_name='pages/about/aboutus.html'),
        name='about_us'),
    url(r'^about/principle/$',
        TemplateView.as_view(template_name='pages/about/principle.html'),
        name='about_principle'),
    url(r'^about/(?P<pk>\d+)/(?P<slug>[\w-]+)/$',
        PageDetailView.as_view(model=About),
        name='about_page_detail'),
    url(r'^stories/(?P<pk>\d+)/(?P<slug>[\w-]+)/$',
        PageDetailView.as_view(model=Story),
        name='story_detail'),
    url(r'^news/(?P<pk>\d+)/(?P<slug>[\w-]+)/$',
        PageDetailView.as_view(model=News),
        name='news_detail'),
    url(r'^events/past/(?P<pk>\d+)/(?P<slug>[\w-]+)/$',
        PageDetailView.as_view(model=PastEvent),
        name='past_event_detail'),
    url(r'^maitreya/(?P<pk>\d+)/(?P<slug>[\w-]+)/$',
        PageDetailView.as_view(model=Maitreya),
        name='maitreya_detail'),
)

urlpatterns += patterns('django.views.generic.list_detail',
    url(r'^about/$',
        PageListView.as_view(model=About),
        name='about_page_index'),
    url(r'^stories/$',
        PageListView.as_view(model=Story),
        name='story_index'),
    url(r'^maitreya/$',
        PageListView.as_view(model=Maitreya),
        name='maitreya_index'),
    url(r'^news/$',
        PageListView.as_view(model=News),
        name='news_index'),
    url(r'^events/past/$',
        PageListView.as_view(model=PastEvent),
        name='past_event_index'),
)

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns(settings.STATIC_URL)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT, show_indexes=True)
