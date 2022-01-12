from flask import redirect, url_for, render_template, request
from app_db import app, db, Client

@app.route('/')
def index():
	return render_template('index.html')

if __name__ == '__main__':
	db.create_all()
	app.run(debug = True, port = 7000, host = '127.0.0.1')