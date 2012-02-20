from django.contrib import admin
from maitreya_van.pages.models import *
from maitreya_van.general.admin import TaggablePageAdmin


class FilterablePageAdmin(TaggablePageAdmin):
    filter_horizontal = ('categories',)


class NewsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(About, TaggablePageAdmin)
admin.site.register(PastEvent, TaggablePageAdmin)
admin.site.register(Story, FilterablePageAdmin)
admin.site.register(Maitreya, FilterablePageAdmin)
admin.site.register(News, NewsAdmin)
