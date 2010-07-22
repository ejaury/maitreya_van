from django.conf.urls.defaults import *

urlpatterns = patterns('maitreya_van.classes.views',
    # Example:
    # (r'^maitreya_van/', include('maitreya_van.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^$', 'index'),
    (r'^(?P<class_id>\d+)/(?P<slug>[\w-]+)/$', 'view_page'),
)
