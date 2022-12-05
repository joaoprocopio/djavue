from http import HTTPStatus
from json import loads

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.handlers.wsgi import WSGIRequest
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET, require_POST

from user.serializer import find_user_to_dict_json, user_to_dict_json
from user.service import find_user


@csrf_exempt
@require_POST
def user_find(request: WSGIRequest) -> object:
    if not request.body:
        return JsonResponse({}, status=HTTPStatus.NO_CONTENT)

    request_body = loads(request.body)

    username = request_body.get("username")

    if not username:
        return JsonResponse({}, status=HTTPStatus.BAD_REQUEST)

    try:
        user = find_user(username)
        user = find_user_to_dict_json(user)

        return JsonResponse(user)

    except User.DoesNotExist:
        return JsonResponse({}, status=HTTPStatus.NOT_FOUND)


@csrf_exempt
@require_POST
def user_login(request: WSGIRequest) -> object:
    if request.user.is_authenticated:
        return JsonResponse({}, status=HTTPStatus.METHOD_NOT_ALLOWED)

    if not request.body:
        return JsonResponse({}, status=HTTPStatus.NO_CONTENT)

    request_body = loads(request.body)

    username = request_body.get("username")
    password = request_body.get("password")

    if not username and password:
        return JsonResponse({}, status=HTTPStatus.BAD_REQUEST)

    user = authenticate(username=username, password=password)

    try:
        login(request, user)
        user = user_to_dict_json(user)

        return JsonResponse(user)

    except AttributeError:
        return JsonResponse({}, status=HTTPStatus.NOT_FOUND)


@require_GET
def user_logout(request: WSGIRequest) -> object:
    if request.user.is_authenticated:
        logout(request)

        return JsonResponse({})

    return JsonResponse({}, status=HTTPStatus.BAD_REQUEST)


@require_GET
def user_whoami(request: WSGIRequest) -> object:
    if request.user:
        user = user_to_dict_json(request.user)

        return JsonResponse(user)

    return JsonResponse({}, status=HTTPStatus.BAD_REQUEST)


def user_register(request: WSGIRequest) -> object:
    return JsonResponse({})


# TODO: deixa o usuário editar seu perfil (username/email/senha)
