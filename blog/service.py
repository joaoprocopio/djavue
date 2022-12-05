from blog.models import Post


def _get_posts():
    return Post.objects.select_related("author").all().order_by("posted_at").reverse()


def _get_post(**kwargs):
    return Post.objects.select_related("author").get(**kwargs)
