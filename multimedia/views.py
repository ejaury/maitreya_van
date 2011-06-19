import os.path
from django.conf import settings
from django.shortcuts import render_to_response
from django.template import RequestContext

from maitreya_van.multimedia.models import Music

def music_gallery_view(request):
    song_url = ''
    if Music.objects.count() > 0:
        music = Music.objects.all()[0]
        song_url = os.path.join(settings.MEDIA_URL, music.file.name)
    context = {
        'title': 'Music Gallery',
        'song_url': song_url,
    }
    return render_to_response('multimedia/music_index.html',
        context, context_instance=RequestContext(request))
