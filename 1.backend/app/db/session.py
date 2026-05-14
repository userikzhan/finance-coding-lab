from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# URL подключения к PostgreSQL
# localhost используется потому что:
# - Alembic запускается из Windows
# - Docker пробрасывает порт 5433 наружу
DATABASE_URL = "postgresql://user:password@localhost:5433/finance"

# Создаём SQLAlchemy engine
engine = create_engine(
    DATABASE_URL
)

# Создаём фабрику сессий
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
