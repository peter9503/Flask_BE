from main import db
from sqlalchemy.dialects.postgresql import UUID
import hashlib
import os
import uuid

nonce = os.getenv('HASH_NONCE')

# db Model create
class account(db.Model):
    __tablename__ = 'account'
    uid      = db.Column(UUID(as_uuid=True) , unique   = True, primary_key = True   , default=uuid.uuid4)
    account  = db.Column(db.String(100)     , unique   = True, nullable    = False  )
    password_hash = db.Column(db.String(256), nullable = False                      )
    email    = db.Column(db.String(100)     , unique   = True, nullable    = False  )
    isDelete = db.Column(db.Boolean         , nullable = False                      )

    def __init__(self,account,password, email) -> None:
        self.account  = str(account)
        self.email    = str(email)
        self.isDelete = False
        self.password_hash = hashlib.sha224((password + nonce).encode('utf-8')).hexdigest()

    def valid_password(self, password) -> bool:
        return hashlib.sha224((password + nonce).encode('utf-8')).hexdigest() == self.password_hash

    