from django.db import models
from photologue.models import Gallery, GalleryUpload
from maitreya_van.general.models import Category

class PhotoGallery(Gallery):
    categories = models.ManyToManyField(Category, limit_choices_to = {
                'content_type__model': 'PhotoGallery',
               })

    class Meta:
        verbose_name_plural = 'Photo Galleries'


class PhotoGalleryUpload(GalleryUpload):
    pass
