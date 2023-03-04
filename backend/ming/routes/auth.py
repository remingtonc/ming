from ..database import engine, models
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from typing import Optional
import logging


async def get_user_from_login(email: str, password: str) -> Optional[models.User]:
    user: Optional[models.User] = None
    async with engine.session() as session:
        async with session.begin():
            stmt = (
                select(models.User)
                .where(models.User.email == email)
                .where(models.User.password == password)
            )
            result = await session.execute(stmt)
            try:
                user = result.scalar_one()
            except:
                logging.exception("No user for %s found with supplied password.", email)
    return user


async def delete_user_session(user_id: int, session_id: str) -> None:
    async with engine.session() as session:
        async with session.begin():
            stmt = (
                select(models.UserSession)
                .where(models.UserSession.user_id == user_id)
                .where(models.UserSession.session_id == session_id)
            )
            result = await session.execute(stmt)
            user_session = result.scalar_one()
            await session.delete(user_session)
            await session.commit()


async def get_user_from_user_session(user_id: int, session_id: str) -> models.User:
    async with engine.session() as session:
        async with session.begin():
            stmt = (
                select(models.UserSession)
                .where(models.UserSession.user_id == user_id)
                .where(models.UserSession.session_id == session_id)
                .options(selectinload(models.UserSession.user))
            )
            result = await session.execute(stmt)
            user_session: models.UserSession = result.scalar_one()
            user: models.User = user_session.user
            return user
