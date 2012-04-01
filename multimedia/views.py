import os.path
from django.conf import settings
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils import simplejson as json
from django.utils.safestring import mark_safe
from django.views.generic import DetailView, ListView

from maitreya_van.multimedia.models import EmbeddedVideo, Music

def music_gallery_view(request):
    playlist = []
    for music in Music.objects.all():
        playlist.append({
            'name': music.song_title,
            'mp3': os.path.join(settings.MEDIA_URL, music.file.name),
        })
    context = {
        'title': 'Music Gallery',
        'playlist': mark_safe(json.dumps(playlist)),
    }
    return render_to_response('multimedia/music_index.html',
        context, context_instance=RequestContext(request))


class VideoDetailView(DetailView):
    context_object_name = 'video'
    model = EmbeddedVideo

    def get_context_data(self, **kwargs):
        context = super(VideoDetailView, self).get_context_data(**kwargs)
        context['title'] = 'Video'
        return context


class VideoListView(ListView):
    model = EmbeddedVideo

    def get_context_data(self, **kwargs):
        context = super(VideoListView, self).get_context_data(**kwargs)
        context['title'] = 'Video'
        return context
