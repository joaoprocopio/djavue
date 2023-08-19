from django.http import JsonResponse

from authentication.serializers import serialize_user


def view_whoami(request):
    user = request.user
    user = serialize_user(user)

    return JsonResponse(user)
