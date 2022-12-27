from django.urls import path

from blog.views import blog_create_post, blog_get_post, blog_get_posts, blog_home_page, blog_publish_post

urlpatterns = [
    path("home_page/", blog_home_page),
    path("author/<int:author_id>/", blog_get_posts),
    path("posts/create/", blog_create_post),
    path("posts/publish/<int:id>", blog_publish_post),
    path("posts/<int:id>/", blog_get_post),
]
