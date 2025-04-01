from django.urls import path

from apps.users.views import logout_logics, login_logics, student_schedule


urlpatterns = [
    path("logout/", logout_logics, name="logout"),
    path("login/", login_logics, name="login"),
    path("student-schedule/<int:pk>/<int:group_pk>", student_schedule, name="student_schedule"),
]
