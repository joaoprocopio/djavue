from django.urls import path

from user.views import user_find, user_login, user_logout, user_register, user_whoami

urlpatterns = [
    path("find/", user_find),
    path("whoami/", user_whoami),
    path("logout/", user_logout),
    path("login/", user_login),
    path("register/", user_register),
]
