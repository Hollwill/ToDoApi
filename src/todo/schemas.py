from pydantic import BaseModel


class TodoListShort(BaseModel):
    id: int
    name: str


class TodoListCreate(BaseModel):
    name: str
