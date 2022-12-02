from django.urls import path

from blog.views import post_fetch, posts_fetch_all

urlpatterns = [
    path("posts/", posts_fetch_all),
    path("post/<id>", post_fetch),
]
