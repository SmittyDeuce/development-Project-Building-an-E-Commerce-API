from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from app import app
from database_models.order_table import OrderTable



ma = Marshmallow(app)

class OrderSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = OrderTable
        include_fk =True

order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)