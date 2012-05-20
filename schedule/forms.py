from django import forms
from django.utils.translation import ugettext_lazy as _
from schedule.models import Event, Occurrence
import datetime
import time

from maitreya_van.add_ons.tinymce.widgets import TinyMCE
from maitreya_van.main.models import Color
from maitreya_van.schedule.models import CalendarGroup
from maitreya_van.common.widgets import ColorSelect


class SpanForm(forms.ModelForm):

    start = forms.DateTimeField(widget=forms.SplitDateTimeWidget)
    end = forms.DateTimeField(widget=forms.SplitDateTimeWidget, help_text = _("The end time must be later than start time."))

    def clean_end(self):
        if self.cleaned_data['end'] <= self.cleaned_data['start']:
            raise forms.ValidationError(_("The end time must be later than start time."))
        return self.cleaned_data['end']


class CalendarGroupForm(forms.ModelForm):
    color_hex = forms.ChoiceField(choices=(), widget=ColorSelect,
        label=_('Color'))

    class Meta:
        model = CalendarGroup
        exclude = ('color',)

    def __init__(self, *args, **kwargs):
        super(CalendarGroupForm, self).__init__(*args, **kwargs)
        self.fields['color_hex'].choices = Color.objects.values_list('hex', 'name')
        if self.instance.pk:
            self.fields['color_hex'].initial = self.instance.color.hex

    def save(self, commit=True):
        group = super(CalendarGroupForm, self).save(commit=False)
        color_hex = self.cleaned_data['color_hex']
        # TODO: Make hex unique
        # Do reverse lookup to find color based on its HEX
        group.color = Color.objects.filter(hex=color_hex)[0]
        if commit:
            group.save()
        return group


class EventForm(SpanForm):
    description = forms.CharField(widget=TinyMCE(attrs={
        'cols': 80,
        'rows': 30,
    }), required=False)

    def __init__(self, hour24=False, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
    
    end_recurring_period = forms.DateTimeField(help_text = _("This date is ignored for one time only events."), required=False)
    
    class Meta:
        model = Event
        exclude = ('creator', 'created_on', 'calendar')
        

class OccurrenceForm(SpanForm):
    description = forms.CharField(widget=TinyMCE(attrs={
        'cols': 80,
        'rows': 30,
    }), required=False)
    
    class Meta:
        model = Occurrence
        exclude = ('original_start', 'original_end', 'event', 'cancelled')


class RuleForm(forms.ModelForm):
    params = forms.CharField(widget=forms.Textarea, help_text=_("Extra parameters to define this type of recursion. Should follow this format: rruleparam:value;otherparam:value."))

    def clean_params(self):
        params = self.cleaned_data["params"]
        try:
            params = params.split(';')
            for param in params:
                param = param.split(':')
                if len(param) == 2:
                    param = (str(param[0]), [int(p) for p in param[1].split(',')])
                    if len(param[1]) == 1:
                        param = (param[0], param[1][0])
        except ValueError:
            raise forms.ValidationError(_("Params format looks invalide"))
        return self.cleaned_data["params"]
