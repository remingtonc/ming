from starlette.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles
from starlette.routing import Route, Mount
from starlette.requests import Request
from starlette.responses import Response, RedirectResponse
from starlette.authentication import requires
from typing import Union
from .middleware import auth_set_cookies, auth_delete_cookies
from ..database import engine
from ..database import models
from . import auth
from typing import Optional
import logging

templates: Jinja2Templates = Jinja2Templates(directory="ming/routes/templates")


async def signup(request: Request) -> Response:
    if request.user.is_authenticated:
        return RedirectResponse("/")
    if request.method == "GET":
        return templates.TemplateResponse("signup.html", {"request": request})
    if request.method == "POST":
        signup_form = await request.form()
        signup_attempted = True
        signup_success = False
        try:
            async with engine.session() as session:
                async with session.begin():
                    new_user = models.User(
                        email=signup_form.get("email"),
                        password=signup_form.get("password"),
                    )
                    session.add(new_user)
                    await session.commit()
            signup_success = True
        except:
            logging.exception('big fail')
            signup_success = False
        return templates.TemplateResponse(
            "signup.html",
            {
                "request": request,
                "signup_success": signup_success,
                "signup_attempted": signup_attempted,
            },
        )


async def login(request: Request) -> Response:
    if request.user.is_authenticated:
        return RedirectResponse("/")
    if request.method == "GET":
        return templates.TemplateResponse("login.html", {"request": request})
    if request.method == "POST":
        if (
            request.cookies.get("ming_user_id", None) is not None
            or request.cookies.get("ming_session_id", None) is not None
        ):
            return RedirectResponse("/logout")
        login_attempted = True
        login_success = False
        login_form = await request.form()
        email = login_form.get("email")
        password = login_form.get("password")
        if not isinstance(email, str) and not isinstance(password, str):
            return templates.TemplateResponse("login.html", {"request": request, "login_success": login_success, "login_attempted": login_attempted})
        else:
            user: Optional[models.User] = await auth.get_user_from_login(email, password)
            if user is not None:
                login_success = True
                response = templates.TemplateResponse("login.html", {"request": request, "login_success": login_success, "login_attempted": login_attempted})
                await auth_set_cookies(response, user)
                return response
            else:
                return templates.TemplateResponse("login.html", {"request": request, "login_success": login_success, "login_attempted": login_attempted})


async def logout(request: Request) -> Response:
    response = RedirectResponse("/")
    return await auth_delete_cookies(request, response)


@requires("authenticated")
async def story(request: Request) -> Response:
    return templates.TemplateResponse("story.html", {"request": request})


async def index(request: Request) -> Response:
    return templates.TemplateResponse("index.html", {"request": request})


def get_routes() -> list[Union[Route, Mount]]:
    return [
        Route("/", endpoint=index, methods=["GET", "POST"]),
        Route("/login", endpoint=login, methods=["GET", "POST"]),
        Route("/logout", endpoint=logout),
        Route("/story", endpoint=story, methods=["GET", "POST"]),
        Route("/signup", endpoint=signup, methods=["GET", "POST"]),
        Mount("/static", StaticFiles(directory="ming/routes/static"), name="static"),
    ]
