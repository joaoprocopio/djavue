def post_to_dict_json(post):
    return {
        "id": post.id,
        "author": {
            "id": post.author.id,
            "name": post.author.get_full_name(),
            "username": post.author.username,
            "first_name": post.author.first_name,
            "last_name": post.author.last_name,
        },
        "slug": post.slug,
        "title": post.title,
        "text": post.text,
        "created_at": post.created_at,
        "posted_at": post.posted_at,
    }
