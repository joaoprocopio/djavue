from http import HTTPStatus
from json import loads

from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET, require_POST
from pydantic import ValidationError

from user.forms import UserForm
from user.serializer import find_user_to_dict_json, user_to_dict_json
from user.service import create_user, find_user


@csrf_exempt
@require_POST
def user_find(request):
    if not request.body:
        return JsonResponse({}, status=HTTPStatus.NO_CONTENT)

    body = loads(request.body)

    username = body.get("username")

    if not username:
        return JsonResponse({}, status=HTTPStatus.BAD_REQUEST)

    try:
        user = find_user(username)
        user = find_user_to_dict_json(user)

        return JsonResponse(user)

    except ObjectDoesNotExist:
        return JsonResponse({}, status=HTTPStatus.NOT_FOUND)


@csrf_exempt
@require_POST
def user_login(request):
    if request.user.is_authenticated:
        return JsonResponse({}, status=HTTPStatus.METHOD_NOT_ALLOWED)

    if not request.body:
        return JsonResponse({}, status=HTTPStatus.NO_CONTENT)

    body = loads(request.body)

    username = body.get("username")
    password = body.get("password")

    if not username and password:
        return JsonResponse({}, status=HTTPStatus.BAD_REQUEST)

    user = authenticate(username=username, password=password)

    try:
        login(request, user)
        user = user_to_dict_json(user)

        return JsonResponse(user)

    except AttributeError:
        return JsonResponse({}, status=HTTPStatus.NOT_FOUND)


@csrf_exempt
@require_POST
def user_register(request):
    if not request.body:
        return JsonResponse({}, status=HTTPStatus.NO_CONTENT)

    if request.user.is_authenticated:
        return JsonResponse({}, status=HTTPStatus.METHOD_NOT_ALLOWED)

    try:
        body = UserForm.parse_raw(request.body)
        body = body.dict()
        user = create_user(**body)
        user = user_to_dict_json(user)

        return JsonResponse(user)

    except ValidationError:
        return JsonResponse({}, status=HTTPStatus.BAD_REQUEST)


@require_GET
def user_logout(request):
    if request.user.is_authenticated:
        logout(request)

        return JsonResponse({})

    return JsonResponse({}, status=HTTPStatus.BAD_REQUEST)


@require_GET
def user_whoami(request):
    if request.user:
        user = user_to_dict_json(request.user)

        return JsonResponse(user)

    return JsonResponse({}, status=HTTPStatus.BAD_REQUEST)
