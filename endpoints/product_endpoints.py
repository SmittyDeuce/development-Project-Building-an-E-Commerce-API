from extensions import db
from database_models.product_table import ProductTable
from schema.product_schema import product_schema, products_schema
from sqlalchemy import select
from flask import request, jsonify, Blueprint
from marshmallow import ValidationError


product_blueprint = Blueprint('product_blueprint', __name__)

#create Product
@product_blueprint.route("/products", methods=["POST"])
def create_products():
    if not request.is_json:
        return jsonify({"error": "Content-Type must be application/json"}), 415

    try:
        product_data = product_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400
    
    new_product = ProductTable(product_name=product_data['product_name'], price=product_data['price'])
    db.session.add(new_product)
    db.session.commit()
    
    return product_schema.jsonify(new_product), 201


#Read products
@product_blueprint.route("/products", methods=["GET"])
def read_products():
    users = db.session.scalars(select(ProductTable)).all()
    if not users:
        return jsonify({"error": "No products found"}), 404
    
    return products_schema.jsonify(users)

#Read Product by ID
@product_blueprint.route("/products/<int:id>", methods=["GET"])
def read_product_id(id):
    
    product = db.session.get(ProductTable, id)
    if not product:
        return jsonify({"error": "product not found"}), 404
    
    return  product_schema.jsonify(product)


#Update Product
@product_blueprint.route("/products/<int:id>", methods=["PUT"])
def update_product(id):
    
    product = db.session.get(ProductTable, id)
    if not product:
        return jsonify({"error": "product not found"}), 404
    
    try:
        product_data = product_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400
    
    product.product_name = product_data["product_name"]
    product.price = product_data["price"]
    
    db.session.commit()
    return product_schema.jsonify(product), 200


#Delete Product
@product_blueprint.route("/products/<int:id>", methods=["DELETE"])
def delete_product(id):
    product = db.session.get(ProductTable, id)
    
    if not product:
        return jsonify({"error": "Invalid product id"}), 400
    
    db.session.delete(product)
    db.session.commit()
    return jsonify({"message": f"Successfully deleted product {id}"}), 200