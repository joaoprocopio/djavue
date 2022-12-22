from django.urls import path

from blog.views import blog_get_post_by_id, blog_get_post_by_user_id, blog_home_page

urlpatterns = [
    path("posts/home_page/", blog_home_page),
    path("posts/<int:id>", blog_get_post_by_id),
    path("posts/<int:user_id>", blog_get_post_by_user_id),
]
