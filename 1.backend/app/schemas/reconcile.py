from pydantic import BaseModel


class ReconcileRequest(BaseModel):

    file_name: str
