from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.admin import AdminSite

admin.site.unregister(Group)

admin.site.site_header = "Панель управления MYWORKS"
admin.site.site_title = "Администрирование MYWORKS"
admin.site.index_title = "Добро пожаловать в админку"

admin_panel = admin
