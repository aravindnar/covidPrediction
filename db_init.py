from flask import Flask,render_template,url_for,request,redirect,session
app=Flask(__name__)
# /from functions import check_login
app.secret_key='test'

from flask_sqlalchemy import SQLAlchemy 
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///users.db'
db=SQLAlchemy(app)

class users(db.Model):
    username=db.Column(db.String(30),primary_key=True)
    password=db.Column(db.String(30))

    def __repr__(self):
        return f"{self.username},{self.password}"

db_obj = (users.query.all())
for i in db_obj:
    print(i)