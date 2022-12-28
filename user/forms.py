from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from email_validator import EmailNotValidError, validate_email
from pydantic import BaseModel, validator


class UserForm(BaseModel):
    username: str
    email: str
    password: str
    first_name: str
    last_name: str

    @validator("email")
    def email_validator(cls, email):
        try:
            validate_email(email)

            return email
        except EmailNotValidError as error:
            raise error

    @validator("password")
    def password_validator(cls, password):
        try:
            validate_password(password)

            return password
        except ValidationError as error:
            raise error
