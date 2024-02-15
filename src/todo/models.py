from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.auth.models import User
from src.database import Base


class TodoList(Base):
    __tablename__ = "todo_todolist"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(225))
    user_id = mapped_column(ForeignKey("user_account.id"))

    user: Mapped[User] = relationship(back_populates="todo_lists")
    items: Mapped[list["TodoListItem"]] = relationship(back_populates="todo_list")


class TodoListItem(Base):
    __tablename__ = "todo_todolistitem"
    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str] = mapped_column(String(255))
    is_completed: Mapped[bool] = mapped_column(default=False)
    todo_list_id = mapped_column(ForeignKey("todo_todolist.id"))

    todo_list: Mapped[TodoList] = relationship(back_populates="items")
