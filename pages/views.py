from django.http import Http404
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.template.defaultfilters import slugify
from maitreya_van.pages.models import *

def index(request):
  return render_to_response('pages/index.html',
                            context_instance=RequestContext(request))

def view_class(request, class_id, slug):
    obj = get_object_or_404(Class, pk=class_id)
    return __render_detail(request, slug, obj)

def view_news(request, news_id, slug):
    obj = get_object_or_404(News, pk=news_id)
    return __render_detail(request, slug, obj)

def view_past_event(request, past_event_id, slug):
    obj = get_object_or_404(PastEvent, pk=past_event_id)
    return __render_detail(request, slug, obj)

def view_teaching(request, teaching_id, slug):
    obj = get_object_or_404(Teaching, pk=teaching_id)
    return __render_detail(request, slug, obj)

def __render_detail(request, slug, obj):
    if not slug == slugify(obj.title):
        raise Http404
    verbose_name = obj.__class__._meta.verbose_name.split()
    model_title = ' '.join([ word.capitalize() for word in verbose_name ])
    return render_to_response('pages/view_page.html', {
          'object': obj,
          'title': model_title,
    }, context_instance=RequestContext(request))
