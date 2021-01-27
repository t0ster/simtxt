from os.path import abspath, dirname, join

from aiohttp import web

import simtxt.tasks
from simtxt.index import Index
from simtxt.utils import register_graphql_handlers


def main() -> None:
    app = register_graphql_handlers(
        app=web.Application(),
        engine_sdl=join(dirname(abspath(__file__)), "simtxt", "sdl.graphql"),
        engine_modules=["simtxt.resolvers"],
        executor_http_endpoint="/graphql",
        executor_http_methods=["POST"],
        graphiql_enabled=True,
    )

    async def create_index(app):
        app["index"] = await Index.create()
        await app["index"].dump()

    app.on_startup.append(create_index)

    # aiohttp_cors.setup(
    #     app,
    #     defaults={
    #         "*": aiohttp_cors.ResourceOptions(allow_headers="*"),
    #     },
    # )

    web.run_app(app)


if __name__ == "__main__":
    main()
