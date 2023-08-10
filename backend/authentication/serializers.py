def anonymous_user_serializer(user):
    return {
        "is_authenticated": user.is_authenticated,
    }


def authenticated_user_serializer(user):
    return {
        "id": user.id,
        "email": user.email,
        "full_name": user.last_name,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "is_authenticated": user.is_authenticated,
    }
