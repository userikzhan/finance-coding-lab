from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from app.db.base import Base


class Reconciliation(Base):

    __tablename__ = "reconciliations"

    id = Column(Integer, primary_key=True, index=True)

    file_name = Column(String, nullable=False)
