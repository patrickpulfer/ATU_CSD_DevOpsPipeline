from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Profile
from portal.models import *


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profile'
    fk_name = 'user'

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(ProfileInline, self).get_inline_instances(request, obj)


class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Ticket)
admin.site.register(Ticket_History)
admin.site.register(Diagnostics_Report)