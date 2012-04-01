import re

from django import forms

from maitreya_van.multimedia import utils
from maitreya_van.multimedia.models import Music, PhotoGallery


class MusicUploadForm(forms.ModelForm):
    class Meta:
        model = Music
        fields = ('file', 'tags')

    def clean_file(self):
        file = self.cleaned_data.get('file')
        if not utils.is_mp3(file.name):
            raise forms.ValidationError('"%s" is not an MP3 file' % file.name)
        return file

    def save(self, commit=True):
        music = super(MusicUploadForm, self).save(commit=False)
        file = self.cleaned_data['file']
        music.title = re.sub(r'\..*$', '', file.name)
        if commit:
            music.save()
        return music


class MusicChangeForm(forms.ModelForm):
    class Meta:
        model = Music
        exclude = ('file',)


class PhotoGalleryUploadForm(forms.ModelForm):
    def clean_title(self):
        title = self.cleaned_data['title']
        if PhotoGallery.objects.filter(title=title).exists():
            raise forms.ValidationError(
                ('A gallery with this title already exists. Please specify '
                 'a different title.'))
        return title
