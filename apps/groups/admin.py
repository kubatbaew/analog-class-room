from django.contrib import admin

from apps.groups.models import Group


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ["title", "subject"]
    search_fields = ["title", "subject"]
