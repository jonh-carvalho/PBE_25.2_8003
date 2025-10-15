from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin

from .models import User


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'display_name', 'email')}),
        ('Profile', {'fields': ('bio', 'avatar_url', 'is_verified', 'role')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    list_display = ('username', 'email', 'display_name', 'is_verified', 'role', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_verified', 'role', 'is_active')
    search_fields = ('username', 'email', 'display_name')
    ordering = ('username',)
