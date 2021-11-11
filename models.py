from typing import Text
import uuid

from sqlalchemy import Column, Integer, MetaData

from database import Base, PostgreSQLUUID


class Account(Base):
    """The Account class corresponds to the "accounts" database table.
    """
    __tablename__ = 'accounts'
    id = Column(PostgreSQLUUID, default=uuid.uuid4, primary_key=True)
    balance: int = Column(Integer)
