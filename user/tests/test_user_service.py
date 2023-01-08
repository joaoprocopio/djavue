from django.core.exceptions import ObjectDoesNotExist
from pytest import raises

from user.service import create_user, find_user


def test_find_user_with_valid_username(user):
    username = user.username

    response = find_user(username)

    assert response.id == user.id
    assert response.username == user.username


def test_find_user_with_valid_email(user):
    username = user.email

    response = find_user(username)

    assert response.id == user.id
    assert response.email == user.email


def test_find_user_with_invalid_username(user):
    with raises(ObjectDoesNotExist):
        username = "uname"

        response = find_user(username)

        assert response


def test_find_user_with_invalid_email(user):
    with raises(ObjectDoesNotExist):
        username = "uname@email.com"

        response = find_user(username)

        assert response


def test_create_user(db, user_data):
    created_user = create_user(**user_data)

    assert created_user.username == user_data.get("username")
