from http import HTTPStatus
from json import loads

from django.core.handlers.wsgi import WSGIRequest
from django.core.paginator import Paginator
from ninja import Router

from djavue.schemas import ErrorSchema
from tasks.schemas import TaskSchema
from tasks.serializers import serialize_task
from tasks.services import filter_tasks, get_task

router = Router()


@router.get("/")
def tasks_view(request: WSGIRequest, page: int = 1, per_page: int = 30):
    tasks = filter_tasks(owner=request.user)

    count = tasks.count()

    tasks = Paginator(tasks, per_page=per_page)
    tasks = tasks.get_page(page)
    tasks = [serialize_task(task) for task in tasks]

    return HTTPStatus.OK, {
        "count": count,
        "tasks": tasks,
    }


@router.get(
    "/{task_id}",
    response={HTTPStatus.OK: TaskSchema, HTTPStatus.NOT_FOUND: ErrorSchema},
)
def task_view(request: WSGIRequest, task_id: int):
    try:
        task = get_task(id=task_id)

        if task.owner.pk != request.user.pk:
            raise Exception

        task = serialize_task(task)

        return HTTPStatus.OK, task

    except Exception:
        return HTTPStatus.NOT_FOUND, {"message": "Not found"}


@router.post("/delete")
def task_delete_view(request: WSGIRequest):
    try:
        body = loads(request.body)
        task_id = body.get("task_id")

        if not task_id:
            raise Exception

        task = get_task(id=task_id)

        if task.owner.pk != request.user.pk:
            raise Exception

        task.is_deleted = True
        task.save()

        task = serialize_task(task)

        return HTTPStatus.OK, task

    except Exception:
        return HTTPStatus.BAD_REQUEST, {}


# TODO: criar tarefa

# TODO: editar tarefa
