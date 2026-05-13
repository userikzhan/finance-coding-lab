from pydantic import BaseModel


class BillingCreate(BaseModel):

    amount: float

    description: str
