from django.contrib import admin
from treemenus.admin import MenuAdmin, MenuItemAdmin
from treemenus.models import Menu
from maitreya_van.navigation.models import MenuItemExtension

class MenuItemExtensionInline(admin.StackedInline):
  model = MenuItemExtension
  max_num = 1

class CustomMenuItemAdmin(MenuItemAdmin):
  inlines = [MenuItemExtensionInline,]

class CustomMenuAdmin(MenuAdmin):
  menu_item_admin_class = CustomMenuItemAdmin

admin.site.unregister(Menu) # Unregister the standard admin options
admin.site.register(Menu, CustomMenuAdmin) # Register the new, customized, admin options

