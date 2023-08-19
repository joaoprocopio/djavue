from http import HTTPStatus

from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.views.decorators.http import require_GET, require_POST

from tasks.serializers import serialize_task
from tasks.services import get_task, get_tasks


@require_GET
def view_tasks(request):
    page = int(request.GET.get("page", 1))
    per_page = int(request.GET.get("per_page", 30))

    tasks = get_tasks()

    count = tasks.count()

    tasks = Paginator(tasks, per_page=per_page)
    tasks = tasks.get_page(page)
    tasks = [serialize_task(task) for task in tasks]

    return JsonResponse(
        {
            "count": count,
            "tasks": tasks,
        }
    )


@require_GET
def view_task(request, task_id):
    try:
        task = get_task(task_id)
        task = serialize_task(task)

        return JsonResponse(task)

    except ObjectDoesNotExist:
        return JsonResponse({}, status=HTTPStatus.NOT_FOUND)


@require_POST
def delete_task(request):
    return JsonResponse({})


# TODO: criar tarefa

# TODO: editar tarefa
