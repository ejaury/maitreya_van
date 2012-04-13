import re

from django import forms

from maitreya_van.multimedia import utils
from maitreya_van.multimedia.models import EmbeddedVideo, Music, PhotoGallery


class EmbeddedVideoForm(forms.ModelForm):
    class Meta:
        model = EmbeddedVideo

    def clean_link(self):
        link = self.cleaned_data.get('link', '')
        if link:
            if 'youtube.com' not in link:
                raise forms.ValidationError('Only a Youtube link can be processed')
        return link.strip()

    def clean_code(self):
        return self.cleaned_data.get('code', '').strip()

    def clean(self):
        cleaned_data = super(EmbeddedVideoForm, self).clean()
        link = cleaned_data.get('link')
        code = cleaned_data.get('embed_code')
        if not code and not link:
            raise forms.ValidationError('You need to specify either a link or embedded code for the video below')

        if link:
            # Only override code if it's not provided, or it's manually changed
            if not code or 'embed_code' not in self.changed_data:
                try:
                    cleaned_data['embed_code'] = utils.create_youtube_embed(link)
                except:
                    raise forms.ValidationError('The link you provided is not valid')

        return cleaned_data


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
