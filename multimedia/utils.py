def is_mp3(filename):
    """Determine if file is an MP3"""
    return filename.endswith('.mp3')

def get_latest_media(limit=5):
    from photologue.models import Photo
    from maitreya_van.multimedia.models import Music
    # TODO: FIx this - find songs as well
    return Photo.objects.order_by('-date_added')[:limit]
