from django.contrib import admin
from maitreya_van.classes.models import Class 
from treemenus.models import Menu, MenuItem

class ClassAdmin(admin.ModelAdmin):
  def save_model(self, request, obj, form, change):
    obj.save()
    # add this object to treemenu list if it's new
    if not change:
      parent_menu_item = MenuItem.objects.get(caption='Classes')
      url = obj.get_absolute_url() 
      menu_item = MenuItem(parent_id=parent_menu_item.id,
                           caption=obj.title,
                           url=obj.get_absolute_url())
      menu_item.save()

  def delete_view(self, request, object_id, extra_context=None):
    # delete menu item only after delete confirmation
    if request.POST:
      klass = Class.objects.get(id=object_id)
      menu_item = MenuItem.objects.get(url=klass.get_absolute_url())
      if menu_item:
        menu_item.delete()
    return super(ClassAdmin, self).delete_view(request, object_id, extra_context)

admin.site.register(Class, ClassAdmin)
