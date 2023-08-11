from tasks.models import Task


def get_tasks():
    return Task.objects.all()


def get_task(id: int):
    return Task.objects.get(id=id)
