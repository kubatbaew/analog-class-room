from django.urls import path

from apps.groups import views


urlpatterns = [
    path("edit-group/<int:pk>", views.edit_group, name="edit_group"),
    path("delete-group/<int:pk>", views.delete_group, name="delete_group"),
    path("group/<int:pk>", views.group_detail, name="detail_group"),
    path("change-banner/<int:pk>", views.change_banner_group, name="change_banner_group")
]
