from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ("email", "username", "first_name", "last_name", "gender", "height", "weight", "is_staff")
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('height', 'weight', 'gender')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
