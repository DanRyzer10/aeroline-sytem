
from utils.db import db
class Passenger(db.Model):
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name=db.Column(db.String(80), nullable=False)
    lastname=db.Column(db.String(80), nullable=False)
    age=db.Column(db.Integer, nullable=False)
    phone=db.Column(db.String(80), nullable=False)
    email=db.Column(db.String(80), nullable=False)
    address=db.Column(db.String(80), nullable=False)

    def __init__(self, name, lastname, age, phone, email, address):
        self.id = 2
        self.name = name
        self.lastname = lastname
        self.age = age
        self.phone = phone
        self.email = email
        self.address = address

    