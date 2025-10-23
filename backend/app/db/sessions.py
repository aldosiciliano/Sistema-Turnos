from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import declarative_base
import os
from dotenv import load_dotenv

load_dotenv()


# ⚙️ Cambiá los valores según tu configuración
DB_USER = "root"
DB_PASS = os.getenv("DB_PASSWORD")
DB_HOST = "localhost"
DB_NAME = "clinica"

DATABASE_URL = f"mysql+aiomysql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}?charset=utf8mb4"

# Crea el motor y la sesión
engine = create_async_engine(DATABASE_URL, echo=False)
AsyncSessionLocal = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
Base = declarative_base()

# Dependencia para obtener la sesión
async def get_session() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        yield session