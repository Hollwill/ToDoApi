from sqlalchemy import select, insert
from sqlalchemy.orm import selectinload

from src.auth.models import User
from src.database import AbstractDAO
from src.todo.models import TodoList
from src.todo.schemas import TodoListCreate as TodoListCreateSchema


class TodoListDAO(AbstractDAO):
    async def get_by_user(self, user: User):
        stmt = select(TodoList).options().where(TodoList.user == user)
        result = await self.session.execute(stmt)
        return result.scalars()

    async def create_for_user(self, user: User, todo_list: TodoListCreateSchema) -> TodoList:
        todo_list_instance = TodoList(user=user, name=todo_list.name)
        self.session.add(todo_list_instance)
        await self.session.commit()
        await self.session.refresh(todo_list_instance, ["name", "id"])
        return todo_list_instance
