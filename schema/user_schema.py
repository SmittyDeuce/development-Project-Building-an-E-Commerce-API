from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from app import app
from database_models.user_table import User

ma = Marshmallow(app)

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        
        
user_schema = UserSchema()
users_schema = UserSchema(many=True)