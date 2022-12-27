from user.serializer import find_user_to_dict_json


def post_to_dict_json(post):
    return {
        "id": post.id,
        "author": find_user_to_dict_json(post.author),
        "title": post.title,
        "text": post.text,
        "created_at": post.created_at,
        "published_at": post.published_at,
    }
