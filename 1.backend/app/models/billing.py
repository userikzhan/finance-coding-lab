from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Float
from sqlalchemy import String

from app.db.base import Base


class Billing(Base):

    __tablename__ = "billings"

    id = Column(Integer, primary_key=True, index=True)

    amount = Column(Float)

    description = Column(String)
