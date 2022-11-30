from django.urls import path

from blog.views import posts_fetch_all

urlpatterns = [
    path("posts/", posts_fetch_all),
]
