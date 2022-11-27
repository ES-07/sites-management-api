from databases import DatabaseURL
from starlette.config import Config
from starlette.datastructures import Secret
import os

PROJECT_NAME='cctv'
VERSION='1.0.0'

POSTGRES_USER = "postgres" #os.environ['POSTGRES_USER']
POSTGRES_PASSWORD = "postgres" #os.environ['POSTGRES_PASSWORD']
POSTGRES_SERVER = "15.237.96.214" #os.environ['POSTGRES_SERVER']
POSTGRES_PORT = "5433"
POSTGRES_DB = "postgres" #os.environ['POSTGRES_DB']

DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"