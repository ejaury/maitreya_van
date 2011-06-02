from django import template
from maitreya_van.utils import nat_sort

register = template.Library()

@register.simple_tag
def next_photo_url(photo, gallery):
  next = photo.get_next_in_gallery(gallery)
  if next:
      return '<a class="nav" title="%s" href="%s">Next</a>' % (next.title, next.get_absolute_url())
  return ""

@register.simple_tag
def previous_photo_url(photo, gallery):
  prev = photo.get_previous_in_gallery(gallery)
  if prev:
      return '<a class="nav" title="%s" href="%s">Previous</a>' % (prev.title, prev.get_absolute_url())
  return ""

@register.filter(name='remainder')
def remainder(input, divisor):
  return int(input) % int(divisor)

@register.filter(name='sort_title')
def sort_by_title(obj_list):
  return nat_sort.natsorted(obj_list, key=lambda obj: obj.title)
