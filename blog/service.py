from blog.models import Post


def create_post(**kwargs):
    post = Post.objects.select_related("author").create(**kwargs)

    return post


def get_posts(**kwargs):
    return Post.objects.select_related("author").filter(**kwargs)


def get_post(**kwargs):
    return Post.objects.select_related("author").get(**kwargs)
