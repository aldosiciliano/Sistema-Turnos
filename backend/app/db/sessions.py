from app.core.config import ASYNC_DB_URL
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession


engine = create_async_engine(
    ASYNC_DB_URL,
    echo = False, # poner True para ver el SQL en consola
    pool_pre_ping = True, # detecta conexiones muertas
    pool_recycle = 3600
)

SessionLocal = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,
    class_=AsyncSession
)

async def get_session() -> AsyncSession:
    async with SessionLocal() as session:
        yield session