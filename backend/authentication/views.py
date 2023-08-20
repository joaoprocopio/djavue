from http import HTTPStatus

from django.core.handlers.wsgi import WSGIRequest
from ninja import Router

from authentication.schemas import AnonymousUserSchema, UserSchema
from authentication.serializers import serialize_anonymous_user, serialize_user

router = Router()


@router.get(
    "whoami",
    response={HTTPStatus.OK: UserSchema, HTTPStatus.UNAUTHORIZED: AnonymousUserSchema},
)
def whoami_view(request: WSGIRequest):
    user = request.user

    if not user.is_authenticated:
        user = serialize_anonymous_user(user)

        return HTTPStatus.UNAUTHORIZED, user

    user = serialize_user(user)

    return HTTPStatus.OK, user
