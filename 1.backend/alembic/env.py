from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context

import sys
from pathlib import Path
import os

from dotenv import load_dotenv

# =========================================================
# Добавляем backend root в PYTHONPATH
# =========================================================
sys.path.append(str(Path(__file__).resolve().parents[1]))

# =========================================================
# Загружаем .env
# =========================================================
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# =========================================================
# Alembic config object
# =========================================================
config = context.config

# =========================================================
# Подставляем DATABASE_URL из .env
# =========================================================
config.set_main_option("sqlalchemy.url", DATABASE_URL)

# =========================================================
# Настройка логирования
# =========================================================
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# =========================================================
# Импорт Base
# =========================================================
from app.db.base import Base

# =========================================================
# Импорт моделей
# =========================================================
from app.models import *

# =========================================================
# Metadata SQLAlchemy
# =========================================================
target_metadata = Base.metadata


# =========================================================
# Offline migrations
# =========================================================
def run_migrations_offline():

    url = config.get_main_option("sqlalchemy.url")

    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


# =========================================================
# Online migrations
# =========================================================
def run_migrations_online():

    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:

        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )

        with context.begin_transaction():
            context.run_migrations()


# =========================================================
# Entry point
# =========================================================
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
