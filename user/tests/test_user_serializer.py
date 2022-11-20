from user.serializer import find_user_to_dict_json, user_to_dict_json


def test_user_to_dict_json(user):
    serialized_user = user_to_dict_json(user)

    assert user.id == serialized_user.get("id")
    assert user.first_name == serialized_user.get("first_name")
    assert user.last_name == serialized_user.get("last_name")
    assert user.email == serialized_user.get("email")


def test_find_user_to_dict_json(user):
    serialized_user = find_user_to_dict_json(user)

    assert user.id == serialized_user.get("id")
    assert user.username == serialized_user.get("username")
    assert user.first_name == serialized_user.get("first_name")
    assert user.is_active == serialized_user.get("is_active")
