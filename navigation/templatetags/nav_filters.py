from django import template

register = template.Library()

@register.filter(name='submenu')
def submenu(menu, path):
  import re
  for menu_item in menu.root_item.children():
    if re.search(menu_item.url, path):
      return menu_item

@register.filter(name='submenu_children')
def submenu_children(menu, path):
  print submenu(menu, path).children()
  return submenu(menu, path).children()

@register.filter(name='submenu_caption')
def submenu_caption(menu, path):
  return submenu(menu, path).caption

