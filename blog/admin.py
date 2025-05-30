from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import AppUser, Blog
from markdownx.admin import MarkdownxModelAdmin

class AppUserAdmin(BaseUserAdmin):
    model = AppUser
    list_display = ('email', 'username', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active', 'is_superuser')
    search_fields = ('email', 'username')
    ordering = ('email',)

    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        ('Dates', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )

admin.site.register(AppUser, BaseUserAdmin)

@admin.register(Blog)
class BlogAdmin(MarkdownxModelAdmin):
    list_display = ('title', 'author', 'published_at')
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ('title', 'author__email')
    list_filter = ('published_at',)
