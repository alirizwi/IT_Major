from flask_sqlalchemy import SQLAlchemy
from app import db
from werkzeug.security import generate_password_hash, \
    check_password_hash

class User(db.Model):
    __tablename__='user'
    entry = db.Column(db.Integer, primary_key=True, autoincrement=True)
	email = db.Column(db.String(80) , unique =True)
    name = db.Column(db.String(80))
    # password = db.Column(db.String)
	def __init__(self, email,name, password):
        self.email = email
        self.name = name
        self.set_password(password)
		# self.name = name

    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)

	def check_password(self, password):
		return check_password_hash(self.pw_hash , password)

	def serialize(self):
		return {'userID':	self.userId,
				'name'	:	self.name,
				'email'	:	self.email,}