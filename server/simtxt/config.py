import dataclasses
import logging
from os import environ

logger = logging.getLogger("simtxt")

@dataclasses.dataclass
class Settings:
    db_uri: str
    index_min_score: float
    lsi_num_topics: int


settings = Settings(
    db_uri=environ.get("SIMTXT_DB_URI", "mongodb://localhost:27017"),
    index_min_score=float(environ.get("SIMTXT_INDEX_MIN_SCORE", 0.1)),
    lsi_num_topics=int(environ.get("SIMTXT_LSI_NUM_TOPIC", 100)),
)

def log_settings():
    for k, v in dataclasses.asdict(settings).items():
        logger.info("%s\t%s", k, v)
