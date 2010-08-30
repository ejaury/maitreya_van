from django.contrib import admin
from maitreya_van.classes.models import Class 
from maitreya_van.general.admin import TaggablePageAdmin

class ClassAdmin(TaggablePageAdmin):
  filter_horizontal = ('categories',)

admin.site.register(Class, ClassAdmin)
