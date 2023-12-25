from sqlalchemy import Sequence
from utils.db import db
class User(db.Model):
    id = db.Column(db.Integer, Sequence('user_id_seq'),primary_key=True,)
    username=db.Column(db.String(80), nullable=False, unique=True)
    password=db.Column(db.String(80), nullable=False) 

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def get_id(self):
        return str(self.id)
    
    def is_authenticated(self):
        return True
    

    