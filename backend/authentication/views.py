from django.http import JsonResponse

from authentication.serializers import (
    anonymous_user_serializer,
    authenticated_user_serializer,
)


def view_whoami(request):
    user = request.user

    if not user.is_authenticated:
        return JsonResponse(anonymous_user_serializer(user))

    return JsonResponse(authenticated_user_serializer(user))
