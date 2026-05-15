from sqlalchemy import Column, Integer, Numeric, String

from app.db.base import Base


class Billing(Base):

    __tablename__ = "billings"

    id = Column(Integer, primary_key=True, index=True)

    amount = Column(Numeric(10, 2))

    description = Column(String)
