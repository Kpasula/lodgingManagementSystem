from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('username', 'email', 'shift', 'staff_phone')
    list_filter = ('username', 'email', 'shift', 'staff_phone')
    fieldsets = (
         ('Account Information', {
            'fields': ('username', 'password', 'is_staff', 'is_superuser')
        }),
         ('Position', {
            'fields': ('shift', 'staff_phone')
        }))
    add_fieldsets = (
         ('Account Information', {
            'fields': ('username', 'password1', 'password2', 'is_staff', 'is_superuser')
        }),
         ('Position', {
            'fields': ('shift', 'staff_phone')
        })

   )


admin.site.register(CustomUser, CustomUserAdmin)
