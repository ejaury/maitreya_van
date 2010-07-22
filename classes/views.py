from django.http import Http404
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.template.defaultfilters import slugify
from maitreya_van.classes.models import Class

def index(request):
  return render_to_response('classes/index.html',
                            context_instance=RequestContext(request))

def view_page(request, class_id, slug):
  klass = get_object_or_404(Class, pk=class_id)
  if not slug == slugify(klass.title):
    raise Http404
  return render_to_response('classes/view_page.html', {
                              'class': klass,
                            },
                            context_instance=RequestContext(request))
