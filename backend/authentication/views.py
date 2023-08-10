from django.http import JsonResponse

from authentication.serializers import (
    serialize_anonymous_user,
    serialize_authenticated_user,
)


def view_whoami(request):
    user = request.user

    if not user.is_authenticated:
        return JsonResponse(serialize_anonymous_user(user))

    return JsonResponse(serialize_authenticated_user(user))
