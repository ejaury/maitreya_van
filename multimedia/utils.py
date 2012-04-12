from django.core.urlresolvers import reverse
from django.utils.text import truncate_words

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
