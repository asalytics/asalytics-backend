from tortoise import Tortoise, run_async
from tortoise.contrib.fastapi import HTTPNotFoundError, register_tortoise
from typing import List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from strawberry.asgi import GraphQL




app = FastAPI()


app = FastAPI()

# graphql_app = GraphQL(schema)
# app.add_route("/analytics", graphql_app)
# app.add_websocket_route("/analytics", graphql_app)


# async def connect_db():
#     await Tortoise.init(
#         db_url = "postgres://postgres:@127.0.0.1:5432/test_db{}",
#         modules = {'models': ['models']}
#     )

# async def main():
#     await connect_db()
#     await Tortoise.generate_schemas()
DATABASE_URL = "postgres://postgres:password@127.0.0.1:5432/test_db"


register_tortoise(
    app,
    db_url = DATABASE_URL,
    modules = {'models': ['models']},
    generate_schemas = True,
    add_exception_handlers = True,
)


# TORTOISE_ORM = {
#     "connections": {"default": DATABASE_URL},
#     "apps": {
#         "models": {
#             "models": ["models"],
#             "default_connection": "default",
#         }
#     },
# }
# print("db Tables successfully created")