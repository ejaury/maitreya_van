from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from maitreya_van.authext.forms import LimitedUserChangeForm


class CustomUserAdmin(UserAdmin):
    reg_admin_change_form = LimitedUserChangeForm
    reg_admin_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'first_name', 'last_name', 'email')}
        ),
    )

    def get_fieldsets(self, request, obj=None):
        if obj and self.is_reg_admin(request.user):
            return self.reg_admin_fieldsets
        return super(CustomUserAdmin, self).get_fieldsets(request, obj)

    def get_form(self, request, obj=None, **kwargs):
        # Use different change form for regular admin
        if obj and self.is_reg_admin(request.user):
            return self.reg_admin_change_form
        return super(CustomUserAdmin, self).get_form(request, obj=obj, **kwargs)

    def queryset(self, request):
        qs = super(CustomUserAdmin, self).queryset(request)
        # Regular admin can only view regular users
        if self.is_reg_admin(request.user):
            return qs.filter(is_staff=False)
        return qs

    def is_reg_admin(self, user):
        return user.is_authenticated() and user.is_staff and not user.is_superuser


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
