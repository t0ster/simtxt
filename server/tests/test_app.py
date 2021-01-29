from simtxt.app import app


async def test_app(aiohttp_client, loop):
    app.on_startup.clear()
    client = await aiohttp_client(app)
    resp = await client.get("/graphiql")
    assert resp.status == 200
