from django.contrib.auth.models import User


def find_user(username):
    if "@" in username:
        user = User.objects.get(email=username.lower())
    else:
        user = User.objects.get(username=username)

    return user
