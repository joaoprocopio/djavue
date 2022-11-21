from django.contrib.auth.models import User


def find_user(username):
    user = _find_user_query(username)

    return user


def _find_user_query(username):
    if "@" in username:
        user = _get_user(email=username.lower())
    else:
        user = _get_user(username=username)

    return user


def _get_user(**kwargs):
    return User.objects.get(**kwargs)
