import logging

import coloredlogs

# # pylint: disable=unused-import
# from logging import *


def init_logging(level=logging.INFO):
    coloredlogs.install(level="DEBUG")
    logging.getLogger().setLevel(logging.INFO)
    logging.getLogger("simtxt").setLevel(level)


# _logger = logging.getLogger("simtxt")
# coloredlogs.install(level="DEBUG", logger=_logger)
# _logger.setLevel(logging.INFO)
