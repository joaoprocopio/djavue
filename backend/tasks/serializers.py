from authentication.serializers import serialize_user


def serialize_task(task):
    return {
        "id": task.id,
        "owner": serialize_user(task.owner),
        "title": task.title,
        "description": task.description,
        "created_at": task.created_at,
        "updated_at": task.updated_at,
        "is_done": task.is_done,
    }
