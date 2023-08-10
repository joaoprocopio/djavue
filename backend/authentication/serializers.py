def serialize_anonymous_user(user):
    return {
        "is_authenticated": user.is_authenticated,
    }


def serialize_authenticated_user(user):
    return {
        "id": user.id,
        "email": user.email,
        "full_name": user.last_name,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "is_authenticated": user.is_authenticated,
    }
