from datetime import datetime
from typing import Optional

from ninja import Schema

from authentication.schemas import UserSchema


class TaskSchema(Schema):
    id: int
    owner: UserSchema
    title: str
    description: str
    created_at: datetime
    updated_at: Optional[datetime]
    is_deleted: bool
