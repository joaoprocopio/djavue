from pydantic import BaseModel, validator


class SignUpUser(BaseModel):
    username: str
    email: str
    password: str
    first_name: str
    last_name: str

    @validator("username")
    def validate_username(cls, username):
        return username

    @validator("email")
    def validate_email(cls, email):
        return email

    @validator("password")
    def validate_password(cls, password):
        return password
