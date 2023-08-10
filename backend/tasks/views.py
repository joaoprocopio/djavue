from django.core.paginator import Paginator
from django.http import JsonResponse

from tasks.models import Task
from tasks.serializers import serialize_task


def view_tasks(request):
    tasks = Task.objects.all()
    # TODO
    # deixar dinâmico com base na request
    paginator = Paginator(tasks, per_page=15)
    page = paginator.get_page(1)
    # TODO
    page = [serialize_task(task) for task in tasks]

    return JsonResponse(
        {
            "count": len(tasks),
            "tasks": page,
        }
    )
