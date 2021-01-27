from functools import partial
from inspect import iscoroutine
from typing import Any, AsyncContextManager, Callable, Dict, List, Optional, Union

import aiohttp_cors
from tartiflette import Engine
from tartiflette_aiohttp import (
    _await_on_startup,
    _cook_on_startup,
    _set_graphiql_handler,
    _set_subscription_ws_handler,
)
from tartiflette_aiohttp._context_factory import default_context_factory
from tartiflette_aiohttp._handler import Handlers, prepare_response


def register_graphql_handlers(
    app: "aiohttp.web.Application",
    engine_sdl: str = None,
    engine_schema_name: str = "default",
    executor_context: Optional[Dict[str, Any]] = None,
    executor_http_endpoint: str = "/graphql",
    executor_http_methods: List[str] = None,
    engine: Engine = None,
    subscription_ws_endpoint: Optional[str] = None,
    subscription_keep_alive_interval: Optional[int] = None,
    graphiql_enabled: bool = False,
    graphiql_options: Optional[Dict[str, Any]] = None,
    engine_modules: Optional[
        List[Union[str, Dict[str, Union[str, Dict[str, str]]]]]
    ] = None,
    context_factory: Optional[AsyncContextManager] = None,
    response_formatter: Optional[
        Callable[
            ["aiohttp.web.Request", Dict[str, Any], Dict[str, Any]],
            "aiohttp.web.Response",
        ]
    ] = None,
) -> "aiohttp.web.Application":
    """Copy of tartiflette_aiohttp.register_graphql_handlers with CORS support enabled
    Register a Tartiflette Engine to an app

    Pass a SDL or an already initialized Engine, not both, not neither.

    Keyword Arguments:
        app {aiohttp.web.Application} -- The application to register to.
        engine_sdl {str} -- The SDL defining your API (default: {None})
        engine_schema_name {str} -- The name of your sdl (default: {"default"})
        executor_context {Optional[Dict[str, Any]]} -- Context dict that will be passed to the resolvers (default: {None})
        executor_http_endpoint {str} -- Path part of the URL the graphql endpoint will listen on (default: {"/graphql"})
        executor_http_methods {list[str]} -- List of HTTP methods allowed on the endpoint (only GET and POST are supported) (default: {None})
        engine {Engine} -- An uncooked engine, or a create_engine coroutines (default: {None})
        subscription_ws_endpoint {Optional[str]} -- Path part of the URL the WebSocket GraphQL subscription endpoint will listen on (default: {None})
        subscription_keep_alive_interval {Optional[int]} -- Number of seconds before each Keep Alive messages (default: {None})
        graphiql_enabled {bool} -- Determines whether or not we should handle a GraphiQL endpoint (default: {False})
        graphiql_options {dict} -- Customization options for the GraphiQL instance (default: {None})
        engine_modules: {Optional[List[Union[str, Dict[str, Union[str, Dict[str, str]]]]]]} -- Module to import (default:{None})
        context_factory: {Optional[AsyncContextManager]} -- asynccontextmanager in charge of generating the context for each request (default: {None})
        response_formatter: {Optional[Callable[[aiohttp.web.Request, Dict[str, Any], Dict[str, Any]], aiohttp.web.Response]]} -- In charger of the transformation of the resulting data into an aiohttp.web.Response (default: {None})
    Raises:
        Exception -- On bad sdl/engine parameter combinaison.
        Exception -- On unsupported HTTP Method.

    Return:
        The app object.
    """
    # pylint: disable=too-many-arguments,too-many-locals
    if not executor_context:
        executor_context = {}

    executor_context["app"] = app

    if not executor_http_methods:
        executor_http_methods = ["GET", "POST"]

    if context_factory is None:
        context_factory = default_context_factory

    context_factory = partial(context_factory, executor_context)

    if not engine:
        engine = Engine()

    if iscoroutine(engine):
        app.on_startup.append(_await_on_startup)
    else:
        app.on_startup.append(
            partial(
                _cook_on_startup,
                engine_sdl,
                engine_schema_name,
                engine_modules,
            )
        )

    app["ttftt_engine"] = engine
    app["response_formatter"] = response_formatter or prepare_response

    cors = aiohttp_cors.setup(app)
    for method in executor_http_methods:
        try:
            route = app.router.add_route(
                method,
                executor_http_endpoint,
                partial(
                    getattr(Handlers, "handle_%s" % method.lower()),
                    context_factory=context_factory,
                ),
            )

            cors.add(route, {"*": aiohttp_cors.ResourceOptions(allow_headers="*")})
        except AttributeError:
            raise Exception("Unsupported < %s > http method" % method)

    _set_subscription_ws_handler(
        app,
        subscription_ws_endpoint,
        subscription_keep_alive_interval,
        context_factory,
    )

    _set_graphiql_handler(
        app,
        graphiql_enabled,
        graphiql_options,
        executor_http_endpoint,
        executor_http_methods,
        subscription_ws_endpoint,
    )

    return app
