from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from extensions import ma
from database_models.user_table import User


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        
        
user_schema = UserSchema()
users_schema = UserSchema(many=True)