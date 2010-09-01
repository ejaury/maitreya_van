from django.contrib import admin
from maitreya_van.pages.models import *
from maitreya_van.general.admin import TaggablePageAdmin

class ClassAdmin(TaggablePageAdmin):
  filter_horizontal = ('categories',)

class PastEventAdmin(TaggablePageAdmin):
  pass

class TeachingAdmin(TaggablePageAdmin):
  filter_horizontal = ('categories',)

admin.site.register(Class, ClassAdmin)
admin.site.register(PastEvent, PastEventAdmin)
admin.site.register(Teaching, TeachingAdmin)
