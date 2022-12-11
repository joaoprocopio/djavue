from pydantic import BaseModel, validator


class UserRegister(BaseModel):
    username: str
    email: str
    password: str
    first_name: str
    last_name: str

    @validator("username")
    def username_validator(cls, username):
        return username

    @validator("email")
    def email_validator(cls, email):
        return email

    @validator("password")
    def password_validator(cls, password):
        return password
