import uuid
from typing import cast

from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sqlalchemy.dialects.postgresql

# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"
SQLALCHEMY_DATABASE_URL = "cockroachdb://root@localhost:26257/bank?sslmode=disable"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
# SessionLocal = sessionmaker(bind=engine)


PostgreSQLUUID = cast(
    "sqlalchemy.types.TypeEngine[uuid.UUID]",
    sqlalchemy.dialects.postgresql.UUID(as_uuid=True),
)

metadata = MetaData()
Base: type = declarative_base(metadata=metadata)