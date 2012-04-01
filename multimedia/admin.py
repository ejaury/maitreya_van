from django.contrib import admin

from maitreya_van.multimedia.forms import *
from maitreya_van.multimedia.models import Music, PhotoGallery, PhotoGalleryUpload, Photo

from photologue.admin import GalleryAdmin, PhotoAdmin as OriginalPhotoAdmin


class MusicAdmin(admin.ModelAdmin):
    add_form = MusicUploadForm
    form = MusicChangeForm

    def get_form(self, request, obj=None, **kwargs):
        """Use special form for music upload"""
        defaults = {}
        if obj is None:
            defaults.update({
                'form': self.add_form,
            })
        defaults.update(kwargs)
        return super(MusicAdmin, self).get_form(request, obj, **defaults)


class PhotoGalleryAdmin(GalleryAdmin):
    filter_horizontal = ('categories', 'photos',)


class PhotoGalleryUploadAdmin(admin.ModelAdmin):
    form = PhotoGalleryUploadForm


# Hide these models from Admin page
from photologue.models import Gallery, GalleryUpload, Photo as OriginalPhoto
admin.site.unregister(Gallery)
admin.site.unregister(GalleryUpload)
admin.site.unregister(OriginalPhoto)

admin.site.register(Music, MusicAdmin)
admin.site.register(PhotoGallery, PhotoGalleryAdmin)
admin.site.register(PhotoGalleryUpload, PhotoGalleryUploadAdmin)
admin.site.register(Photo, OriginalPhotoAdmin)
