from http import HTTPStatus

from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator
from django.http import JsonResponse

from tasks.serializers import serialize_task
from tasks.services import get_task, get_tasks


def view_tasks(request):
    tasks = get_tasks()
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


def view_task(request, task_id):
    try:
        task = get_task(task_id)
        task = serialize_task(task)

        return JsonResponse(task)

    except ObjectDoesNotExist:
        return JsonResponse({}, status=HTTPStatus.NOT_FOUND)
