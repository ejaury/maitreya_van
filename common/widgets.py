from django.conf import settings
from django.forms import Widget
from django.forms.util import flatatt
from django.utils import simplejson as json
from django.utils.safestring import mark_safe


class ColorSelect(Widget):
    class Media:
        css = {
            'all': (settings.STATIC_URL + 'css/widgets.css',)
        }
        js = (settings.STATIC_URL + "js/widgets/colorselect.js",)

    def __init__(self, attrs=None, choices=()):
        super(ColorSelect, self).__init__(attrs)
        self.choices = list(choices)

    def render(self, name, value, attrs=None, choices=()):
        if value is None: value = ''
        final_attrs = self.build_attrs(attrs, name=name)
        if value != '':
            # Only add the 'value' attribute if a value is non-empty.
            final_attrs['value'] = value
        output = [u'<input type="hidden"%s>' % flatatt(final_attrs)]
        output.append(u'</input>')
        output.append(u'<script type="text/javascript">colorSelect.init("%(id)s", %(choices)s);</script>' % {
            'id': final_attrs['id'],
            'choices': json.dumps(self.choices),
        })
        return mark_safe(u'\n'.join(output))
