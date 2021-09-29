from main import db
import hashlib
import os

nonce = os.getenv('NONCE')

# db Model create
class account(db.Model):
    __tablename__ = 'account'
    uid      = db.Column(db.Integer         , unique   = True, primary_key = True   )
    username = db.Column(db.String(100)     , unique   = True, nullable    = False  )
    password_hash = db.Column(db.String(256), nullable = False                     )
    email    = db.Column(db.String(100)     , unique   = True, nullable    = False  )
    isDelete = db.Column(db.Boolean         , nullable = False                      )

    def __init__(self,uid,username,password, email, gender) -> None:
        self.uid      = int(uid)
        self.username = str(username)
        self.email    = str(email)
        self.isDelete = False
        self.password_hash = hashlib.sha224(password + nonce).hexdigest()

    def valid_password(self, password) -> bool:
        return hashlib.sha224(password + nonce).hexdigest() == self.password_hash

    