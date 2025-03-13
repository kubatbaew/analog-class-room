from django.contrib import admin

from django.contrib.auth import get_user_model

User = get_user_model()


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['email']
    search_fields = ['email']
    exclude = [
        "password",
        "is_superuser",
        "is_staff",
        "user_permissions",
        "groups",
    ]
