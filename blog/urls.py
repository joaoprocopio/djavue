from django.urls import path

from blog.views import blog_post, blog_posts

urlpatterns = [
    path("posts/", blog_posts),
    path("posts/<int:id>", blog_post),
]
