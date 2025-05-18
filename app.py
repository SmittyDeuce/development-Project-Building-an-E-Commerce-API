from __future__ import annotations
from password import password
from flask import Flask, request,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy.orm import DeclarativeBase, relationship, mapped_column, Mapped
from sqlalchemy import ForeignKey, Table, Column, String, Integer, select
from marshmallow import ValidationError
from typing import List, Optional
import os

#initialize the app
app = Flask(__name__)

#MySql data base config
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqlconnector://root:{password}@localhost/ecommerce_api'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#Creating base class
class Base(DeclarativeBase):
    pass

#initialize extension
db = SQLAlchemy(model_class=Base) # Set up SQLAlchemy using custom Declarative Base
db.init_app(app) # Link db object to Flask App
ma = Marshmallow(app) # Initialize MArshmallow for schema serialization