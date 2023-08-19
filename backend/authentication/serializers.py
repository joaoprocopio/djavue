def serialize_user(user):
    return (
        {
            "id": user.id,
            "email": user.email,
            "first_name": user.first_name,
            "username": user.username,
            "is_authenticated": user.is_authenticated,
        }
        if user.is_authenticated
        else {
            "is_authenticated": user.is_authenticated,
        }
    )
