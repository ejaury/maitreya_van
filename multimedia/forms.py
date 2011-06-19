import re
from django import forms

from maitreya_van.multimedia.models import Music


class MusicUploadForm(forms.ModelForm):
    class Meta:
        model = Music
        fields = ('file', 'tags')

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
