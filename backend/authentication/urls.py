from django.urls import path

from authentication import views

urlpatterns = [
    path("whoami/", views.view_whoami),
]
