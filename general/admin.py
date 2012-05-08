from django.contrib import admin

from maitreya_van.general.forms import BasePageAdminForm
from maitreya_van.general.models import Category
from maitreya_van.utils.admin import delete_selected_models

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

class BasePageAdmin(admin.ModelAdmin):
    actions = [delete_selected_models,]
    form = BasePageAdminForm
    prepopulated_fields = {"slug": ("title",)}

    class Media:
        js = ("js/tiny_mce/tiny_mce.js", "js/admin/utils.js")

    def get_actions(self, request):
        actions = super(BasePageAdmin, self).get_actions(request)
        #
        # disable default delete_selected action since delete_selected uses
        # queryset's delete() method, and not our custom delete() defined in the model
        #
        del actions['delete_selected']
        return actions


class TaggablePageAdmin(BasePageAdmin):
    pass

admin.site.register(Category, CategoryAdmin)
