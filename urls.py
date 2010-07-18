from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^maitreya_van/', include('maitreya_van.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^$', 'maitreya_van.main.views.index'),
    (r'^about/', include('maitreya_van.about.urls')),
    (r'^classes/', include('maitreya_van.classes.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {
      'document_root': '/home/edwin/maitreya_van/assets/', 'show_indexes': True
    }),
)
