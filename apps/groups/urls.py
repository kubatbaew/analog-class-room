from django.urls import path

from apps.groups import views


urlpatterns = [
    path("edit-group/<int:pk>", views.edit_group, name="edit_group"),
]
