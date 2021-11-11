from typing import List

from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy_cockroachdb import run_transaction

from fastapi import Depends, FastAPI, HTTPException
import uvicorn

import crud, models, schemas, database

app = FastAPI()


# Dependency
def get_db():
    db = sessionmaker(bind=database.engine)
    try:
        yield db
    finally:
        db.close_all()

@app.get("/accounts/", response_model=List[schemas.Account])
# def read_accounts(skip: int = 0, limit: int = 100, s: sessionmaker = Depends(get_db)):
#     with s() as db:
#         accounts = crud.get_accounts(db, skip=skip, limit=limit)
def read_accounts(skip: int = 0, limit: int = 100, db: sessionmaker = Depends(get_db)):
    accounts = run_transaction(db, lambda db: crud.get_accounts(db, skip=skip, limit=limit))
    return accounts

@app.post("/accounts/", response_model=schemas.Account)
def create_account(account: schemas.AccountCreate, db: sessionmaker = Depends(get_db)):
    # new_user = crud.create_account(db=db, account=account) ## standard FastAPI
    db_account = run_transaction(db, lambda db: crud.create_account(db=db, account=account))
    print(f"New account has {db_account.id=} and {db_account.balance=}")
    return db_account

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)