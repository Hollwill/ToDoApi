from sqlalchemy import select

from src.auth.models import User
from src.database import AbstractDAO


class UserDAO(AbstractDAO):
    async def get_by_username(self, username):
        stmt = select(User).where(User.username == username)
        result = await self.session.execute(stmt)
        return result.scalar()
