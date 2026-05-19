# =====================================================
# Работа с:
# - JWT access token
# - hash password
# - verify password
# =====================================================

from datetime import datetime, timedelta

# JWT
from jose import jwt

# bcrypt hashing
from passlib.context import CryptContext

# Central settings
from app.core.settings import settings


# =====================================================
# Настройка bcrypt
#
# schemes=["bcrypt"]
# → использовать bcrypt для hash
#
# deprecated="auto"
# → старые схемы будут помечаться автоматически
# =====================================================

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


# =====================================================
# SECRET_KEY и ALGORITHM из settings
#
# Раньше было:
#
# SECRET_KEY = "supersecret"
#
# Это плохо:
# - секрет хранится в коде
# - небезопасно
#
# Теперь:
# .env
# → settings
# → security.py
# =====================================================

SECRET_KEY = settings.SECRET_KEY

ALGORITHM = settings.ALGORITHM


# =====================================================
# Создание JWT access token
#
# data:
# payload токена
#
# Пример:
# {
#     "sub": "user_id"
# }
# =====================================================

def create_access_token(data: dict):

    # Копируем payload
    to_encode = data.copy()

    # Время жизни токена
    expire = datetime.utcnow() + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )

    # Добавляем exp
    to_encode.update({
        "exp": expire
    })

    # Создаём JWT
    encoded_jwt = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return encoded_jwt


# =====================================================
# Hash password
#
# plain password:
# qwerty123
#
# →
# bcrypt hash
# =====================================================

def hash_password(password: str) -> str:

    return pwd_context.hash(password)


# =====================================================
# Verify password
#
# Сравнение:
# plain password
# vs
# hashed password
#
# True / False
# =====================================================

def verify_password(
    plain_password: str,
    hashed_password: str
) -> bool:

    return pwd_context.verify(
        plain_password,
        hashed_password
    )
