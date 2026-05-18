# =========================================================
# Central import file for SQLAlchemy models
#
# Этот файл нужен для:
# - централизованного импорта моделей
# - удобной работы Alembic
# - корректной регистрации моделей в Base.metadata
#
# Благодаря этому можно использовать:
#
# from app.models import *
#
# вместо множества отдельных import
# =========================================================


# =========================================================
# User model
# =========================================================
from app.models.user import User


# =========================================================
# Refresh token model
#
# Используется для:
# - JWT refresh tokens
# - session management
# - logout/revoke tokens
# =========================================================
from app.models.refresh_token import RefreshToken


# =========================================================
# Financial transactions model
#
# Используется для:
# - платежей
# - переводов
# - accounting logic
# - reconciliation
# =========================================================
from app.models.transaction import Transaction
