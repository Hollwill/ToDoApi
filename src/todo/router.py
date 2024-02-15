from typing import Annotated

from fastapi import Depends, APIRouter

from src.auth.dependency import get_current_active_user
from src.auth.schemas import User
from src.todo.database import TodoListDAO
from src.todo.schemas import TodoListShort, TodoListCreate

router = APIRouter()


@router.get("/todo_list")
async def get_todo_list(
        todo_lists: Annotated[TodoListDAO, Depends()], current_user: Annotated[User, Depends(get_current_active_user)]
) -> list[TodoListShort]:
    async with todo_lists:
        return await todo_lists.get_by_user(current_user)

@router.post("/todo_list")
async def create_todo_list(
        todo_list: TodoListCreate, todo_lists: Annotated[TodoListDAO, Depends()], current_user: Annotated[User, Depends(get_current_active_user)]
) -> TodoListShort:
    return await todo_lists.create_for_user(current_user, todo_list)
