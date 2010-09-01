from django import forms
from django.conf import settings
from django.contrib import admin
from maitreya_van.add_ons.tinymce.widgets import TinyMCE
from maitreya_van.general.models import BasePage, Category
from maitreya_van.utils.admin import delete_selected_models
from treemenus.models import Menu, MenuItem
from treemenus.utils import get_parent_choices

class BasePageAdminForm(forms.ModelForm):
  content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
  class Meta:
    model = BasePage

class CategoryAdmin(admin.ModelAdmin):
  prepopulated_fields = {"slug": ("name",)}

class BasePageAdmin(admin.ModelAdmin):
  actions = [delete_selected_models,]
  form = BasePageAdminForm
  prepopulated_fields = {"slug": ("title",)}

  class Media:
    js = (
      "js/tiny_mce/tiny_mce.js",
    )

  def get_actions(self, request):
    actions = super(BasePageAdmin, self).get_actions(request)
    #
    # disable default delete_selected action since delete_selected uses
    # queryset's delete() method, and not our custom delete() defined in the model
    #
    del actions['delete_selected']
    return actions

  def get_form(self, request, obj=None, **kwargs):
    form = super(BasePageAdmin, self).get_form(request, obj, **kwargs)
    menu = Menu.objects.get(name=getattr(settings, 'MAIN_MENU_NAME', 'Main'))
    # override foreign key's default choice field to show list of menu items in tree form
    form.base_fields['parent_menu_item'].choices=get_parent_choices(menu, obj)
    return form

class TaggablePageAdmin(BasePageAdmin):
  pass

admin.site.register(Category, CategoryAdmin)
