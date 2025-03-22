from django.contrib import admin

from apps.works.models import Work


@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = ["title", "group"]
    search_fields = ["title", "group"]
