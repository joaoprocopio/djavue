from django.urls import path

from authentication import views

urlpatterns = [
    path("whoami", views.current_user_view),
]
