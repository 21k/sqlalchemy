#export FLASK_ENV='development'
#flask run

import os
import json
from flask import Flask,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, instance_relative_config=True)
app.config.from_mapping(
    SECRET_KEY='dev',
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
    SQLALCHEMY_DATABASE_URI='mysql+mysqldb://root@localhost:3306/sql_test',
)
db = SQLAlchemy(app)
db.create_all()

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.String(20), primary_key=True)
    username = db.Column(db.String(255))
    create_time = db.Column(db.String(255))

@app.route('/api/list')
def hello():
    order_by = request.args.get('order_by')
    result=User.query.order_by(order_by).all()
    return json.dumps([row.id for row in result] or [])
