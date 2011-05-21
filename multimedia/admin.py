from django.contrib import admin
from maitreya_van.multimedia.models import PhotoGallery, PhotoGalleryUpload
from photologue.admin import GalleryAdmin

class PhotoGalleryAdmin(GalleryAdmin):
    filter_horizontal = ('categories', 'photos',)

class PhotoGalleryUploadAdmin(admin.ModelAdmin):
    pass

admin.site.register(PhotoGallery, PhotoGalleryAdmin)
admin.site.register(PhotoGalleryUpload)
