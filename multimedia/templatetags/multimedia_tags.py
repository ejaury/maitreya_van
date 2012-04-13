import re
import urlparse

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


# Source: http://djangosnippets.org/snippets/2554/
class YoutubeNode(template.Node):
    """Convenient tag, allowing only having a normal watch link, from yotube,
    embed video in html."""

    def __init__(self, parsed_link):
        self.parsed_link = parsed_link

    def render(self, context):
        link = self.parsed_link.render(context)
        url = urlparse.urlparse(link)
        params = urlparse.parse_qs(url.query)
        vid_id = params.get('v', [''])[0]
        replace_it = re.compile('watch$')
        link = replace_it.sub('embed/', url.path) + vid_id
        video = """<iframe width="560" height="315" src="%s" frameborder="0" allowfullscreen></iframe>""" % link
        return video

@register.tag
def embed(parser, token):
    """Given a youtube link, convert it to an embed code"""
    parsed_link = parser.parse(('endembed',))
    # first token it's closing tag. delete_first_token
    # just delete it - del self.tokens[0];)
    parser.delete_first_token()
    return YoutubeNode(parsed_link)
