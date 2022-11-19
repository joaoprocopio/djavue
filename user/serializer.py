def find_user_to_dict_json(user):
    return {
        "id": user.id,
        "username": user.username,
        "is_active": user.is_active,
    }


def user_to_dict_json(user):
    return {
        "id": user.id,
        "name": user.get_full_name(),
        "username": user.username,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "email": user.email,
    }
