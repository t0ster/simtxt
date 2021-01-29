import logging

import coloredlogs


def init_logging(level=logging.INFO):
    coloredlogs.install(level="DEBUG")
    logging.getLogger().setLevel(logging.INFO)
    logging.getLogger("simtxt").setLevel(level)
