from django.urls import path

from apps.works.views import list_works_by_group


urlpatterns = [
    path("list-works/<int:pk>", list_works_by_group, name="list_works_by_group"),
]
