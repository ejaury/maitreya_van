from django import template

register = template.Library()

@register.filter(name='submenu_children')
def submenu_children(menu, path):
  print 'adfasdf'
  import re
  print 'PATH: ' + path
  for menu_item in menu.root_item.children():
    print menu_item.url
    if re.search(menu_item.url, path):
      return menu_item.children()
