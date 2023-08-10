def serialize_task(task):
    return {
        "title": task.title,
        "description": task.description,
        "created_at": task.created_at,
        "updated_at": task.updated_at,
        "is_done": task.is_done,
    }
