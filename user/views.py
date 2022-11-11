from json import loads

from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from user.serializer import user_to_dict_json


@csrf_exempt
@require_POST
def user_login(request):
    request_body = loads(request.body)

    username = request_body.get("username")
    password = request_body.get("password")

    user = authenticate(username=username, password=password)

    if user:
        login(request, user)
        user = user_to_dict_json(user)

        return JsonResponse(user, status=200)

    return JsonResponse({}, status=404)


def user_logout(request):
    if request.user.is_authenticated:
        logout(request)

        return JsonResponse({}, status=200)

    return JsonResponse({}, status=404)


def user_whoami(request):
    user = (
        {
            "user": user_to_dict_json(request.user),
            "authenticated": True,
        }
        if request.user.is_authenticated
        else {
            "authenticated": False,
        }
    )

    return JsonResponse(user, status=200)
