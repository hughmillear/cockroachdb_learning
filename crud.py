from typing import List
import uuid

from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy_cockroachdb import run_transaction

import models, schemas

## temp
from math import floor
import random
## temp

def get_accounts(db: Session, skip: int = 0, limit: int = 100) -> List[schemas.Account]:
    return db.query(models.Account).offset(skip).limit(limit).all()

def create_account(db: Session, account: schemas.AccountCreate):
    """Create N new accounts with random account IDs and account balances.
    """
    db_account = models.Account(balance=account.balance)
    # return db.add(db_account) ## WONT WORK - the db.add() call needs to happen before the return
    db.add(db_account)
    return db_account


#### Tutorial code

# def create_accounts(session, num):
#     """Create N new accounts with random account IDs and account balances.
#     """
#     print("Creating new accounts...")
#     new_accounts = []
#     while num > 0:
#         account_id: uuid.uuid4 = uuid.uuid4()
#         account_balance = floor(random.random()*1_000_000)
#         new_accounts.append(models.Account(id=account_id, balance=account_balance))
#         seen_account_ids.append(account_id)
#         print("Created new account with id {0} and balance {1}.".format(
#             account_id, account_balance))
#         num = num - 1
#     session.add_all(new_accounts)


# def transfer_funds_randomly(session, one, two):
#     """Transfer money between two accounts.
#     """
#     source = session.query(models.Account).filter(models.Account.id == one).first()
#     dest = session.query(models.Account).filter(models.Account.id == two).first()
#     print("Random account balances:\nAccount {0}: {1}\nAccount {2}: {3}".format(
#         one, source.balance, two, dest.balance))

#     amount = floor(source.balance/2)
#     print("Transferring {0} from account {1} to account {2}...".format(
#         amount, one, two))

#     # Check balance of the first account.
#     if source.balance < amount:
#         raise "Insufficient funds in account {0}".format(one)
#     else:
#         source.balance -= amount
#         dest.balance += amount

#     print("Transfer complete.\nNew balances:\nAccount {0}: {1}\nAccount {2}: {3}".format(
#         one, source.balance, two, dest.balance))


# def delete_accounts(session, num):
#     """Delete N existing accounts, at random.
#     """
#     print("Deleting existing accounts...")
#     delete_ids = []
#     while num > 0:
#         delete_id = random.choice(seen_account_ids)
#         delete_ids.append(delete_id)
#         seen_account_ids.remove(delete_id)
#         num = num - 1

#     accounts = session.query(models.Account).filter(models.Account.id.in_(delete_ids)).all()

#     for account in accounts:
#         print("Deleted account {0}.".format(account.id))
#         session.delete(account)


# def parse_cmdline():
#     parser = ArgumentParser()
#     parser.add_argument("url", help="Enter your node\'s connection string\n")
#     opt = parser.parse_args()
#     return opt

# if __name__ == '__main__':

#     opt = parse_cmdline()
#     conn_string = opt.url
#     # For cockroach demo:
#     # postgres://demo:<demo_password>@127.0.0.1:26257?sslmode=require
#     # For CockroachCloud:
#     # postgres://<username>:<password>@<globalhost>:26257/<cluster_name>.defaultdb?sslmode=verify-full&sslrootcert=<certs_dir>/<ca.crt>
#     try:
#         db_uri = os.path.expandvars(conn_string)
#         db_uri = urllib.parse.unquote(db_uri)

#         psycopg_uri = db_uri.replace(
#             'postgresql://', 'cockroachdb://').replace(
#                 'postgres://', 'cockroachdb://').replace(
#                     '26257?', '26257/bank?')
#         # The "cockroachdb://" prefix for the engine URL indicates that we are
#         # connecting to CockroachDB using the 'cockroachdb' dialect.
#         # For more information, see
#         # https://github.com/cockroachdb/sqlalchemy-cockroachdb.
#         engine = create_engine(psycopg_uri)
#     except Exception as e:
#         print('Failed to connect to database.')
#         print('{0}'.format(e))

#     seen_account_ids: List[uuid.UUID] = []

#     run_transaction(sessionmaker(bind=engine),
#                     lambda s: create_accounts(s, 100))

#     from_id = random.choice(seen_account_ids)
#     to_id = random.choice([id for id in seen_account_ids if id != from_id])

#     run_transaction(sessionmaker(bind=engine),
#                     lambda s: transfer_funds_randomly(s, from_id, to_id))

#     run_transaction(sessionmaker(bind=engine), lambda s: delete_accounts(s, 5))
