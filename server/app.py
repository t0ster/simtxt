from aiohttp import web

from simtxt.app import app
from simtxt.config import log_settings
from simtxt.logg import init_logging

init_logging()
log_settings()
web.run_app(app)
