import re
import urlparse

from django.core.urlresolvers import reverse
from django.utils.text import truncate_words

def create_youtube_embed(link):
    """Convert a Youtube link into an embed code."""
    # Source: http://djangosnippets.org/snippets/2554/
    url = urlparse.urlparse(link)
    params = urlparse.parse_qs(url.query)
    vid_id = params.get('v', [''])[0]
    replace_it = re.compile('watch$')
    link = '%(scheme)s://%(netloc)s%(path)s%(query)s' % {
        'scheme': url.scheme,
        'netloc': url.netloc,
        'path': replace_it.sub('embed/', url.path),
        'query': vid_id,
    }
    return """<iframe width="560" height="315" src="%s" frameborder="0" allowfullscreen></iframe>""" % link

def is_mp3(filename):
    """Determine if file is an MP3"""
    return filename.endswith('.mp3')

def get_latest_media(limit=5):
    from photologue.models import Photo
    from maitreya_van.multimedia.models import EmbeddedVideo
    # TODO: FIx this - find songs as well
    photos = Photo.objects.order_by('-date_added')[:limit]
    videos = EmbeddedVideo.objects.order_by('-timestamp')[:limit]
    media = []
    word_lim = 4
    for photo in photos:
        media.append({
            'type': 'Photo',
            'title': truncate_words(photo.title, word_lim),
            'url': reverse('pl-photo', kwargs={'slug': photo.title_slug}),
            'timestamp': photo.date_added
        })

    for vid in videos:
        media.append({
            'type': 'Video',
            'title': truncate_words(vid.title, word_lim),
            'url': reverse('video_detail', kwargs={'slug':vid.slug}),
            'timestamp': vid.timestamp,
        })

    media = sorted(media, key=lambda m: m['timestamp'], reverse=True)
    return media[:limit]
