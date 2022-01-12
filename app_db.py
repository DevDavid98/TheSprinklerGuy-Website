from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///client.db'
db = SQLAlchemy(app)

class Client(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column('name', db.String())
	email = db.Column('email', db.String())
	message = db.Column('message', db.Text())