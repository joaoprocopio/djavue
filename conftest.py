from unittest.mock import ANY

import pytest
from django.contrib.auth.models import AnonymousUser
from django.contrib.sessions.middleware import SessionMiddleware
from model_bakery import baker


@pytest.fixture
def user(db, faker):
    username = faker.user_name()
    password = "password"
    user = baker.make(
        "auth.User",
        username=username,
        first_name=faker.first_name(),
        last_name=faker.last_name(),
        email=f"{username}@email.com",
    )
    user.set_password(password)
    user.save()

    return user


@pytest.fixture
def user_data(faker):
    username = faker.user_name()
    password = "password"

    user = {
        "username": username,
        "first_name": faker.first_name(),
        "last_name": faker.last_name(),
        "email": f"{username}@email.com",
        "password": password,
    }

    return user


@pytest.fixture
def anonymous_user():
    return AnonymousUser()


@pytest.fixture
def session_middleware():
    return SessionMiddleware(get_response=ANY)
