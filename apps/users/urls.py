from django.urls import path

from apps.users.views import logout_logics, login_logics


urlpatterns = [
    path("logout/", logout_logics, name="logout"),
    path("login/", login_logics, name="login"),
]
