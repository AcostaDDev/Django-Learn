from pydantic import BaseModel, Field

class AccountSerializer(BaseModel):
    owner: str
    amount: float = Field(..., gt=0.0)