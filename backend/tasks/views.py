from http import HTTPStatus
from json import loads

from django.core.handlers.wsgi import WSGIRequest
from django.core.paginator import Paginator
from django.http import JsonResponse
from ninja import Router

from tasks.serializers import serialize_task
from tasks.services import filter_tasks, get_task

router = Router()


@router.get("/")
def view_tasks(request: WSGIRequest):
    page = int(request.GET.get("page", 1))
    per_page = int(request.GET.get("per_page", 30))

    try:
        tasks = filter_tasks(owner_id=request.user.pk)

    except Exception:
        return JsonResponse({})

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


@router.get("/{task_id}")
def view_task(request: WSGIRequest, task_id):
    try:
        task = get_task(id=task_id)
        task = serialize_task(task)

        return JsonResponse(task)

    except Exception:
        return JsonResponse({}, status=HTTPStatus.NOT_FOUND)


@router.post("/delete")
def delete_task(request: WSGIRequest):
    try:
        user = request.user
        body = loads(request.body)
        task_id = body.get("task_id")

        if not task_id:
            raise Exception

        task = get_task(id=task_id)

        if task.owner.pk != user.pk:
            raise Exception

        task.is_deleted = True
        task.save()

        return JsonResponse(serialize_task(task))

    except Exception:
        return JsonResponse({}, status=HTTPStatus.BAD_REQUEST)


# TODO: criar tarefa

# TODO: editar tarefa
