from typing import Annotated

from fastapi import Depends, APIRouter

from src.auth.dependency import get_current_active_user
from src.auth.schemas import User
from src.todo.database import TodoListDAO
from src.todo.schemas import TodoListShort

router = APIRouter()


@router.get("/todo_list")
async def todo_list(
        todo_lists: Annotated[TodoListDAO, Depends()], current_user: Annotated[User, Depends(get_current_active_user)]
) -> list[TodoListShort]:
    return await todo_lists.get_by_user(current_user)
