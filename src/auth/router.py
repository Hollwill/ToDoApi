from typing import Annotated

from fastapi import Depends, APIRouter, HTTPException
from fastapi.security import  OAuth2PasswordRequestForm

from src.auth.database import UserDAO
from src.auth.dependency import get_current_active_user, oauth2_scheme
from src.auth.schemas import User


router = APIRouter()


@router.get("/items/")
async def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"token": token}


@router.post("/token")
async def login(users: Annotated[UserDAO, Depends()], form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    async with users:
        user = await users.get_by_username(form_data.username)
        if not user:
            raise HTTPException(status_code=400, detail="Incorrect username or password")
        # TODO: hashed_password = fake_hash_password(form_data.password)
        hashed_password = form_data.password
        if not hashed_password == user.hashed_password:
            raise HTTPException(status_code=400, detail="Incorrect username or password")

        return {"access_token": user.username, "token_type": "bearer"}

@router.get("/users/me")
async def read_users_me(
    current_user: Annotated[User, Depends(get_current_active_user)]
):
    return current_user
