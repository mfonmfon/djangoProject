from django.contrib import admin
from .models import Customer
from  django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.
# admin.site.register(Customer)

@admin.register(Customer)
class Admin(BaseUserAdmin):
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "usable_password", "password1", "password2"),
            },
        ),
    )


