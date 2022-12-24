from django.urls import path

from blog.views import blog_get_post_by_id, blog_get_posts_by_author_id, blog_home_page

urlpatterns = [
    path("home_page/", blog_home_page),
    path("user/<int:author_id>", blog_get_posts_by_author_id),
    path("<int:id>", blog_get_post_by_id),
]
