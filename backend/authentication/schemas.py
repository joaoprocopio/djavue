from ninja import Schema


class UserSchema(Schema):
    id: int
    email: str
    username: str
    first_name: str
    is_authenticated: bool
    is_active: bool


class AnonymousUserSchema(Schema):
    id: int
    username: str
    is_authenticated: bool
    is_active: bool
