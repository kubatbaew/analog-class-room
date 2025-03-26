from django.contrib import admin

from apps.news.models import Notification


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ["group", "teacher"]
    search_fields = ["group"]
