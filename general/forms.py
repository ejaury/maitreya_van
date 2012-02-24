from django import forms

from maitreya_van.add_ons.tinymce.widgets import TinyMCE
from maitreya_van.general.models import BasePage
from maitreya_van.general.utils import get_menu_item_choices

from treemenus.models import MenuItem


class BasePageAdminForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    parent_menu_item = forms.ModelChoiceField(queryset=MenuItem.objects.all())

    class Meta:
        model = BasePage

    def __init__(self, *args, **kwargs):
        super(BasePageAdminForm, self).__init__(*args, **kwargs)
        self.fields['parent_menu_item'].choices = get_menu_item_choices(self.instance)
