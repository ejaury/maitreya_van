from django.contrib import admin
from schedule.forms import RuleForm

from schedule.models import Calendar, CalendarGroup, Event, CalendarRelation, Rule
from schedule.forms import CalendarGroupForm


class CalendarAdminOptions(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ['name']


class CalendarGroupAdmin(admin.ModelAdmin):
    form = CalendarGroupForm
    fieldsets = (
        (None, {
            'fields': ('name', 'color_hex', 'members'),
        }),
    )


class RuleAdmin(admin.ModelAdmin):
    form = RuleForm

admin.site.register(Calendar, CalendarAdminOptions)
admin.site.register(CalendarGroup, CalendarGroupAdmin)
admin.site.register(Rule, RuleAdmin)
admin.site.register([Event, CalendarRelation])
