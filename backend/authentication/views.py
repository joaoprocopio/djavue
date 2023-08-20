from django.http import JsonResponse
from ninja import Router

from authentication.serializers import serialize_user

router = Router()


@router.get("whoami")
def view_whoami(request):
    user = request.user
    user = serialize_user(user)

    return JsonResponse(user)
