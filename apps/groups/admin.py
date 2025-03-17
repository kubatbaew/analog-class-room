from django.contrib import admin

from apps.groups.models import Group


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ["title", "group_title"]
    search_fields = ["title", "group_title"]
