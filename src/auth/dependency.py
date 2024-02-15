from typing import Annotated

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from starlette import status

from src.auth.database import UserDAO
from src.auth.models import User as UserModel
from src.auth.schemas import User as UserSchema

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")


async def get_user(username: str, users: UserDAO):
    async with users:
        return await users.get_by_username(username)


async def fake_decode_token(token, users):
    # This doesn't provide any security at all
    # Check the next version
    user = await get_user(token, users)
    return user


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)], users: UserDAO = Depends()):
    user = await fake_decode_token(token, users)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user


async def get_current_active_user(
        current_user: Annotated[UserModel, Depends(get_current_user)]
) -> UserSchema:
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user
