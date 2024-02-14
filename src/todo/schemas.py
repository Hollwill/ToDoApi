from pydantic import BaseModel


class TodoListShort(BaseModel):
    id: int
    name: str