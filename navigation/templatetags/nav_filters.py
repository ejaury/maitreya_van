import re
from django import template

register = template.Library()

@register.filter(name='submenu')
def submenu(menu, path):
  for menu_item in menu.root_item.children():
    patterns = menu_item.extension.selected_patterns
    if patterns:
      for pattern in patterns.splitlines():
        if re.compile(pattern).match(path):
          return menu_item

@register.filter(name='submenu_children')
def submenu_children(menu, path):
  return submenu(menu, path).children()

@register.filter(name='submenu_caption')
def submenu_caption(menu, path):
  return submenu(menu, path).caption

@register.filter(name='match_path')
def match_path(path, patterns):
  if patterns:
    for pattern in patterns.splitlines():
      # special case for Home
      if not path and pattern == '^/$':
        return True
      if path and re.compile(pattern).match(path):
        return True
  return False
