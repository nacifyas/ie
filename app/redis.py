from aredis_om import get_redis_connection, Migrator
from app.settings import Settings


redis = get_redis_connection(
    url=str(Settings().redis_db),
    encoding=Settings().encoding,
    decode_responses=True
)
