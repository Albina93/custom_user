from django.contrib import admin
from userapp import models
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class CustomUserAdmin(UserAdmin):
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Custom Field Heading',
            {
                'fields': (
                    'age',
                    'displayname',
                    'url'
                ),
            },
        ),
    )

admin.site.register(models.CustomUser, CustomUserAdmin)