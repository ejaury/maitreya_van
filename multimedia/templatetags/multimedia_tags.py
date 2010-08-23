from django import template

register = template.Library()

@register.simple_tag
def next_photo_url(photo, gallery):
  next = photo.get_next_in_gallery(gallery)
  if next:
      return '<a title="%s" href="%s">Next >></a>' % (next.title, next.get_absolute_url())
  return ""

@register.simple_tag
def previous_photo_url(photo, gallery):
  prev = photo.get_previous_in_gallery(gallery)
  if prev:
      return '<a title="%s" href="%s"><< Previous</a>' % (prev.title, prev.get_absolute_url())
  return ""

@register.filter(name='remainder')
def remainder(input, divisor):
  return int(input) % int(divisor)
