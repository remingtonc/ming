from starlette.config import Config
from starlette.datastructures import Secret

DEFAULT_DATABASE_NAME: str = "ming"
DEFAULT_DATABASE_PORT: int = 5432

# Config will be read from environment variables and/or ".env" files.
config: Config = Config(".env", env_prefix="BACKEND_")

DEBUG: bool = config("DEBUG", default=False)
DATABASE_HOST: str = config("DATABASE_HOST")
DATABASE_USER: str = config("DATABASE_USER")
DATABASE_PASSWORD: Secret = config("DATABASE_PASSWORD", cast=Secret)
DATABASE_NAME: str = config("DATABASE_NAME", default=DEFAULT_DATABASE_NAME)
DATABASE_PORT: int = config("DATABASE_PORT", cast=int, default=DEFAULT_DATABASE_PORT)
