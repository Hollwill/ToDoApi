from sqlalchemy import select

from src.auth.models import User
from src.database import AbstractDAO


class TodoListDAO(AbstractDAO):
    async def get_by_user(self, user: User):
        stmt = select(TodoListDAO).where(User.id == user.id)
        result = await self.session.execute(stmt)
        return result.scalars()
