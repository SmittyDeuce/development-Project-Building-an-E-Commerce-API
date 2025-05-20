from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from extensions import ma
from database_models.order_table import OrderTable




class OrderSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = OrderTable
        include_fk =True

order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)