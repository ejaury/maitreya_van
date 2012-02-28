from django import forms
from django.db import transaction

from maitreya_van.add_ons.tinymce.widgets import TinyMCE
from maitreya_van.general.models import BasePage
from maitreya_van.general.utils import get_menu_item_choices
from maitreya_van.navigation.models import MenuItemExtension

from treemenus.models import MenuItem


class BasePageAdminForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    parent_menu_item = forms.ModelChoiceField(queryset=MenuItem.objects.all(),
        help_text = 'Menu item that this page belongs to (e.g. Dance Class page belongs to "Classes" section)')

    class Meta:
        model = BasePage

    def __init__(self, *args, **kwargs):
        super(BasePageAdminForm, self).__init__(*args, **kwargs)
        self.fields['parent_menu_item'].choices = get_menu_item_choices(self.instance)

        if self.instance.pk:
            self.fields['parent_menu_item'].initial = self.instance.menu_item.parent

    @transaction.commit_on_success
    def save(self, commit=True):
        try:
            # so we can get form.save_m2m()
            page = super(BasePageAdminForm, self).save(commit=False)
            page.save()
            url = page.get_absolute_url()
            menu_kwargs = {
                'parent': self.cleaned_data['parent_menu_item'],
                'caption': page.title,
                'url': url,
            }
            if not self.instance.menu_item:
                menu_item = MenuItem(**menu_kwargs)
                menu_item.save()
                self.instance.menu_item = menu_item
                self.instance.save()
            else:
                for attr, val in menu_kwargs.items():
                    setattr(self.instance.menu_item, attr, val)
                self.instance.menu_item.save()

            menu_item_ext, created = MenuItemExtension.objects.get_or_create(
                menu_item=self.instance.menu_item)
            menu_item_ext.selected_patterns = '^%s$' % url
            menu_item_ext.save()
        except Exception:
            transaction.rollback()
            raise
        else:
            return page
