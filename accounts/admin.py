from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

from .forms import *


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = ['full_name', 'email', 'is_admin']
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('full_name', 'email', 'password')
                }),
        ('Personal Info', {'fields': ('is_active',)
                           }),
        ('Permissions', {'fields': ('is_admin',)
                         }),
    )
    add_fieldsets = (
        (
            None, {'fields': ('email', 'password', 're_password', 'full_name')}
        ),
    )
    search_fields = ('email', 'first_name')
    ordering = ('email',)
    filter_horizontal = ()


admin.site.unregister(Group)
