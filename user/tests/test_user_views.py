from json import dumps, loads

from user.views import user_login, user_logout, user_whoami


def test_user_login_with_valid_user(rf, user, session_middleware):
    request_body = dumps(
        {
            "username": user.username,
            "password": "password",
        }
    )

    request = rf.post(
        "/api/user/login/",
        request_body,
        "application/json",
    )

    session_middleware.process_request(request)
    response = user_login(request)
    response_content = loads(response.content)

    assert user.id == response_content.get("id")


def test_user_login_with_invalid_user(rf, user, session_middleware):
    request_body = dumps(
        {
            "username": "",
            "password": "",
        }
    )

    request = rf.post(
        "/api/user/login/",
        request_body,
        "application/json",
    )

    session_middleware.process_request(request)
    response = user_login(request)
    response_content = loads(response.content)

    assert response_content == {}


def test_user_logout_with_logged_user(rf, user, session_middleware):
    request = rf.get("/api/user/logout/")
    request.user = user
    session_middleware.process_request(request)
    response = user_logout(request)
    response_content = loads(response.content)

    assert response_content == {}


def test_user_logout_with_anonymous_user(rf, anonymous_user, session_middleware):
    request = rf.get("/api/user/logout")
    request.user = anonymous_user
    session_middleware.process_request(request)
    response = user_logout(request)
    response_content = loads(response.content)

    assert response_content == {}


def test_user_whoami_with_logged_user(rf, user):
    request = rf.get("/api/user/whoami/")
    request.user = user
    response = user_whoami(request)
    response_content = loads(response.content)

    assert response_content.get("authenticated") is True


def test_user_whoami_with_anonymous_user(rf, anonymous_user):
    request = rf.get("/api/user/whoami/")
    request.user = anonymous_user
    response = user_whoami(request)
    response_content = loads(response.content)

    assert response_content.get("authenticated") is False
