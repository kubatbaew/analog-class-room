from django.urls import path

from apps.works.views import list_works_by_group, detail_work, create_done_work, works_students, done_work_student, done_work_add_grade, create_work_to_group, delete_work


urlpatterns = [
    path("list-works/<int:pk>", list_works_by_group, name="list_works_by_group"),
    path("work/<int:pk>", detail_work, name="detail_work"),
    path("create_done_work/<int:pk>", create_done_work, name="create_done_work"),
    path("works-students/<int:pk>", works_students, name="works_students"),
    path("done_work_student/<int:pk>", done_work_student, name="detail_done_work"),
    path("add-grade-work/<int:pk>", done_work_add_grade, name="done_work_add_grade"),
    path("create_work_for_group/<int:pk>", create_work_to_group, name="create_work_to_group"),
    path("delete-work/<int:pk><int:group_pk>", delete_work, name="delete_work"),
]
