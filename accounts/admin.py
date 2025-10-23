from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser

class CustomUserAdmin(BaseUserAdmin):
    model = CustomUser
    list_display = ('email', 'phone', 'country', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active', 'country')
    ordering = ('email',)
    search_fields = ('email', 'phone', 'country')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Личная информация', {'fields': ('avatar', 'phone', 'country')}),
        ('Права доступа', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'avatar', 'phone', 'country', 'is_staff', 'is_active')}
        ),
    )

admin.site.register(CustomUser, CustomUserAdmin)  # ✅ всё правильно
