from databases import DatabaseURL
from starlette.config import Config
from starlette.datastructures import Secret
import os

PROJECT_NAME='cctv'
VERSION='1.0.0'

POSTGRES_USER = os.environ['POSTGRES_USER']
POSTGRES_PASSWORD = os.environ['POSTGRES_PASSWORD']
POSTGRES_SERVER = os.environ['POSTGRES_SERVER']
POSTGRES_PORT = "5433"
POSTGRES_DB = os.environ['POSTGRES_DB']

DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"