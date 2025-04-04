from django.urls import path

from apps.groups import views


urlpatterns = [
    path("edit-group/<int:pk>", views.edit_group, name="edit_group"),
    path("delete-group/<int:pk>", views.delete_group, name="delete_group"),
    path("group/<int:pk>", views.group_detail, name="detail_group"),
    path("change-banner/<int:pk>", views.change_banner_group, name="change_banner_group"),
    path("group-users/<int:pk>", views.group_users, name="group_users"),
    path("student-add-group/<int:pk>", views.add_student_to_group, name="add_student_to_group"),
    path("create_group/", views.create_group, name="create_group"),
]
