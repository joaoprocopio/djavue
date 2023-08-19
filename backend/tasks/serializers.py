from authentication.serializers import serialize_user
from tasks.models import Task


def serialize_task(task: Task):
    return {
        "id": task.pk,
        "owner": serialize_user(task.owner),
        "title": task.title,
        "description": task.description,
        "created_at": task.created_at,
        "updated_at": task.updated_at,
        "is_done": task.is_done,
    }
