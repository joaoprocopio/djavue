from django.urls import path

from blog.views import blog_home_page, blog_post

urlpatterns = [
    path("home_page/", blog_home_page),
    path("posts/<int:id>", blog_post),
]
