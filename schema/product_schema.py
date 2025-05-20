from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from extensions import ma
from database_models.product_table import ProductTable


class ProductSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ProductTable
        include_fk = True
        
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)