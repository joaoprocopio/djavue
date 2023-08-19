from tasks.models import Task


def filter_tasks(**kwargs):
    return Task.objects.filter(**kwargs)


def get_task(id: int):
    return Task.objects.get(id=id)
