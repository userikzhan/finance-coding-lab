# =========================================================
# Async SQLAlchemy engine для FastAPI
# =========================================================
# Используется для:
#
# - асинхронной работы с PostgreSQL
# - FastAPI dependency injection
# - repositories/services
# - async CRUD операций
# - future scaling
#
# Async SQLAlchemy:
# позволяет НЕ блокировать event loop FastAPI
#
# Это особенно важно при:
# - большом количестве запросов
# - работе с API
# - finance/reconciliation processing
# - background tasks
# =========================================================

from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncSession
)

# =========================================================
# sessionmaker создаёт фабрику сессий
# =========================================================
# Через sessionmaker FastAPI получает
# новые подключения к БД
#
# Каждая request/session:
# получает собственный AsyncSession
# =========================================================
from sqlalchemy.orm import sessionmaker

# =========================================================
# Импортируем central settings
# =========================================================
# settings:
# - читает данные из .env
# - валидирует их через Pydantic
# - хранит все config values централизованно
#
# Теперь НЕ нужно:
# os.getenv(...)
#
# Используем:
# settings.DATABASE_URL
# settings.SECRET_KEY
# и т.д.
# =========================================================
from app.core.config import settings


# =========================================================
# DATABASE_URL из .env
# =========================================================
#
# В .env:
#
# DATABASE_URL=postgresql://user:password@localhost:5433/finance
#
# Но Async SQLAlchemy требует:
#
# postgresql+asyncpg://
#
# Поэтому делаем replace()
#
# Было:
# postgresql://
#
# Станет:
# postgresql+asyncpg://
#
# Пример:
#
# postgresql://user:password@localhost:5433/finance
#
# →
#
# postgresql+asyncpg://user:password@localhost:5433/finance
#
# asyncpg:
# это async driver для PostgreSQL
# =========================================================
DATABASE_URL = settings.DATABASE_URL.replace(
    "postgresql://",
    "postgresql+asyncpg://"
)


# =========================================================
# Создаём async engine
# =========================================================
#
# engine:
# главный объект подключения к PostgreSQL
#
# Через engine SQLAlchemy:
# - открывает соединения
# - отправляет SQL запросы
# - управляет connection pool
#
# echo=True:
# показывает SQL запросы в консоли
#
# Полезно во время разработки:
#
# SELECT ...
# INSERT ...
# UPDATE ...
#
# В production обычно:
# echo=False
#
# future=True:
# включает modern SQLAlchemy API
#
# pool_pre_ping=True:
# проверяет живо ли соединение
# перед использованием
#
# Это важно для:
# - Docker
# - long-running apps
# - reconnect scenarios
# =========================================================
engine = create_async_engine(
    DATABASE_URL,

    # Показывать SQL запросы
    echo=True,

    # SQLAlchemy 2.x style
    future=True,

    # Проверка соединений
    pool_pre_ping=True
)


# =========================================================
# SessionLocal
# =========================================================
#
# SessionLocal:
# фабрика async-сессий
#
# Через неё FastAPI получает соединения
# с PostgreSQL
#
# bind=engine:
# привязываем engine
#
# class_=AsyncSession:
# используем async sessions
#
# expire_on_commit=False:
# объект НЕ "умирает" после commit()
#
# Иначе после commit():
#
# user.email
#
# мог бы вызвать:
# DetachedInstanceError
#
# autoflush=False:
# SQLAlchemy НЕ будет автоматически
# отправлять изменения в БД
#
# Это даёт:
# - больше контроля
# - меньше неожиданных flush
# =========================================================
SessionLocal = sessionmaker(
    bind=engine,

    # Async SQLAlchemy session
    class_=AsyncSession,

    # Объекты остаются доступными
    # после commit()
    expire_on_commit=False,

    # Без автоматического flush
    autoflush=False
)


# =========================================================
# Dependency для FastAPI
# =========================================================
#
# Использование:
#
# @router.get("/")
# async def route(db: AsyncSession = Depends(get_db)):
#
# FastAPI:
# - создаёт session
# - передаёт её в endpoint
# - закрывает автоматически
#
# yield:
# позволяет корректно закрыть session
# после завершения request
# =========================================================
async def get_db():

    # Создаём новую async session
    async with SessionLocal() as session:

        # Передаём session в endpoint/service
        yield session
