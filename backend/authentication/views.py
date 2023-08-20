from django.http import JsonResponse
from ninja import Router

from authentication.serializers import serialize_user

router = Router()


@router.get("whoami")
def whoami_view(request):
    user = request.user
    user = serialize_user(user)

    return JsonResponse(user)
