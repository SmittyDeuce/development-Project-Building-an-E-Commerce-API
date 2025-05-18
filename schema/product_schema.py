from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from app import app
from database_models.product_table import ProductTable

ma = Marshmallow(app)


class ProductSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ProductTable
        include_fk = True
        
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)