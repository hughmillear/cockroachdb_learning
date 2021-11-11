from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel

from database import Base

class AccountCreate(BaseModel):
    balance: int

class Account(AccountCreate):
    id: UUID
    balance: int

    class Config:
        orm_mode = True
