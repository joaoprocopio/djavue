from tasks.models import Task


def filter_tasks(**kwargs):
    return Task.objects.filter(**kwargs)


def get_task(**kwargs):
    return Task.objects.get(**kwargs)
