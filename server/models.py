# server/models.py

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

# optional: define naming conventions for constraints/indexes
metadata = MetaData()

# create the SQLAlchemy extension
db = SQLAlchemy(metadata=metadata)

# Define a simple Pet model
class Pet(db.Model):
    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    species = db.Column(db.String)

# Example of more complex model with constraints
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False, index=True)
    email = db.Column(db.String(120), unique=True)
    verified = db.Column(db.Boolean, default=False)
