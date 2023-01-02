from pydantic import BaseModel


class PostForm(BaseModel):
    author_id: int
    title: str
    text: str
