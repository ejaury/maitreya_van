from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User


class LimitedUserChangeForm(UserChangeForm):
    """Change form for User for regular admin with limited change permissions."""
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    def __init__(self, *args, **kwargs):
        super(LimitedUserChangeForm, self).__init__(*args, **kwargs)
        # Wider fields
        for name, field in self.fields.iteritems():
            if name != 'username':
                field.widget.attrs['class'] = 'vTextField'
