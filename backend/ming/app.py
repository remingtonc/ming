from starlette.applications import Starlette
from . import database, config, routes


async def global_startup() -> None:
    pass


async def global_shutdown() -> None:
    await database.engine.engine.dispose()


app: Starlette = Starlette(
    routes=routes.get_routes(),
    middleware=routes.get_middleware(),
    on_startup=[global_startup],
    on_shutdown=[global_shutdown],
    debug=config.DEBUG,
)
