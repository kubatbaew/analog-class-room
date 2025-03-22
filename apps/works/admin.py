from django.contrib import admin

from apps.works.models import Work, DoneWork


@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = ["title", "group"]
    search_fields = ["title", "group"]


@admin.register(DoneWork)
class DoneWorkAdmin(admin.ModelAdmin):
    list_display = ["student"]
    search_fields = ["student"]