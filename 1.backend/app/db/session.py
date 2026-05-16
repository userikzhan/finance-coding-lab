# Async SQLAlchemy engine для FastAPI
# Используется для асинхронной работы с PostgreSQL

from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncSession
)

# sessionmaker создаёт фабрику сессий
from sqlalchemy.orm import sessionmaker

# Импортируем central settings
# settings читает данные из .env
from app.core.config import settings


# ---------------------------------------------------
# DATABASE_URL из .env
#
# Было:
# postgresql://
#
# Async SQLAlchemy требует:
# postgresql+asyncpg://
#
# Поэтому делаем replace()
# ---------------------------------------------------

DATABASE_URL = settings.DATABASE_URL.replace(
    "postgresql://",
    "postgresql+asyncpg://"
)


# ---------------------------------------------------
# Создаём async engine
#
# engine — это главный объект подключения
# к PostgreSQL
#
# echo=True:
# показывает SQL запросы в консоли
# удобно для разработки
# ---------------------------------------------------

engine = create_async_engine(
    DATABASE_URL,
    echo=True
)


# ---------------------------------------------------
# SessionLocal
#
# Фабрика async-сессий
#
# Через неё FastAPI получает соединения
# с PostgreSQL
#
# expire_on_commit=False:
# объект не "умирает" после commit()
# ---------------------------------------------------

SessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)
