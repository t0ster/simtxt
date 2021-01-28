import logging
from os.path import abspath, dirname, join

from aiohttp import web

import simtxt.tasks
from simtxt.config import log_settings
from simtxt.db import init_db
from simtxt.index import init_index
from simtxt.logging import init_logging
from simtxt.utils import register_graphql_handlers

init_logging()


def main() -> None:
    log_settings()
    app = register_graphql_handlers(
        app=web.Application(),
        engine_sdl=join(dirname(abspath(__file__)), "simtxt", "sdl.graphql"),
        engine_modules=["simtxt.resolvers"],
        executor_http_endpoint="/graphql",
        executor_http_methods=["POST"],
        graphiql_enabled=True,
    )

    async def on_startup(app):
        await init_db()
        await init_index()
        # app["index"] = await Index.create()
        # await app["index"].dump()

    app.on_startup.append(on_startup)

    web.run_app(app)


if __name__ == "__main__":
    main()
