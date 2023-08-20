from django.contrib.auth.models import AnonymousUser, User


def serialize_user(user: User):
    return {
        "id": user.pk,
        "email": user.email,
        "username": user.username,
        "first_name": user.first_name,
        "is_authenticated": user.is_authenticated,
        "is_active": user.is_active,
    }


def serialize_anonymous_user(user: AnonymousUser):
    return {
        "id": user.pk,
        "username": user.username,
        "is_authenticated": user.is_authenticated,
        "is_active": user.is_active,
    }
