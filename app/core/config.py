from databases import DatabaseURL
from starlette.config import Config
from starlette.datastructures import Secret
import os

PROJECT_NAME='cctv'
VERSION='1.0.0'

config = Config(".env")

SECRET_KEY = config("SECRET_KEY", cast=Secret, default="CHANGEME")

""" POSTGRES_USER = config(os.environ['POSTGRES_USER'], cast=str, default="postgres")
POSTGRES_PASSWORD = config(os.environ['POSTGRES_PASSWORD'], cast=Secret, default="postgres")
POSTGRES_SERVER = config(os.environ['POSTGRES_SERVER'], cast=str, default="postgres")
POSTGRES_PORT = "5433"
POSTGRES_DB = config(os.environ['POSTGRES_DB'], cast=str, default="postgres") """

POSTGRES_USER = config("postgres", cast=str, default="postgres")
POSTGRES_PASSWORD = config("postgres", cast=Secret, default="postgres")
POSTGRES_SERVER = config("15.237.96.214", cast=str, default="postgres")
POSTGRES_PORT = "5433"
POSTGRES_DB = config("postgres", cast=str, default="postgres")

DATABASE_URL = config(
  "DATABASE_URL",
  cast=str,
  default=f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"
)