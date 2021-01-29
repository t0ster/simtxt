from os.path import abspath, dirname, join

from aiohttp import web

from simtxt.db import db
from simtxt.index import init_index
from simtxt.utils import register_graphql_handlers

app = register_graphql_handlers(
    app=web.Application(),
    engine_sdl=join(dirname(abspath(__file__)), "sdl.graphql"),
    engine_modules=["simtxt.resolvers"],
    executor_http_endpoint="/graphql",
    executor_http_methods=["POST"],
    graphiql_enabled=True,
)


async def on_startup(app):
    await db.init_db()
    await init_index()


app.on_startup.append(on_startup)
