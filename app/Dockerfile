FROM python:3.9

ARG POSTGRES_USER=$POSTGRES_USER
ARG POSTGRES_PASSWORD=$POSTGRES_PASSWORD
ARG POSTGRES_SERVER=$POSTGRES_SERVER
ARG POSTGRES_PORT=$POSTGRES_PORT
ARG POSTGRES_DB=$POSTGRES_DB

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

RUN pip install psycopg2-binary

COPY . .

CMD ["uvicorn", "api.routes.main:app", "--host", "0.0.0.0", "--port", "8000"]

EXPOSE 8000

