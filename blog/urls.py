from django.urls import path

from blog.views import post_fetch, posts_fetch

urlpatterns = [
    path("posts/", posts_fetch),
    path("post/<id>", post_fetch),
]
