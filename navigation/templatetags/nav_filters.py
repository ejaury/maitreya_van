from django import template

register = template.Library()

@register.filter(name='submenu_children')
def submenu_children(menu, path):
  import re
  for menu_item in menu.root_item.children():
    if re.search(menu_item.url, path):
      return menu_item.children()
