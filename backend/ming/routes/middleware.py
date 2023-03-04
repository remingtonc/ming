from starlette.authentication import (
    AuthCredentials,
    AuthenticationBackend,
    AuthenticationError,
    SimpleUser,
)
from starlette.responses import Response
from starlette.requests import Request
from starlette.middleware import Middleware
from starlette.middleware.authentication import AuthenticationMiddleware
from sqlalchemy import select, delete
from sqlalchemy.orm import selectinload
from .. import database
from ..database.engine import session
from ..database.models import User, UserSession
from uuid import UUID
from . import auth


async def auth_set_cookies(response: Response, user: User):
    async with database.engine.session() as session:
        async with session.begin():
            new_user_session = UserSession(user_id=user.user_id)
            session.add(new_user_session)
            await session.commit()
            response.set_cookie("ming_user_id", str(new_user_session.user_id))
            response.set_cookie("ming_session_id", str(new_user_session.session_id))
    return response


async def auth_delete_cookies(request: Request, response: Response):
    response.delete_cookie("ming_user_id")
    response.delete_cookie("ming_session_id")
    if request.user.is_authenticated:
        user_id = request.cookies.get("ming_user_id")
        session_id = request.cookies.get("ming_session_id")
        if user_id is None or session_id is None:
            raise AuthenticationError("wtf is going on")
        user_id = int(user_id)
        await auth.delete_user_session(user_id, session_id)
    return response


class CookieSessionAuthBackend(AuthenticationBackend):
    async def authenticate(self, conn) -> tuple[AuthCredentials, SimpleUser]:
        user_id = conn.cookies.get("ming_user_id", None)
        session_id = conn.cookies.get("ming_session_id", None)
        if not user_id or not session_id:
            return
        user_id = int(user_id)
        try:
            user = await auth.get_user_from_user_session(user_id, session_id)
            return AuthCredentials(["authenticated"]), SimpleUser(user.email)
        except:
            raise AuthenticationError("Invalid session.")


def get_middleware() -> list[Middleware]:
    return [Middleware(AuthenticationMiddleware, backend=CookieSessionAuthBackend())]
