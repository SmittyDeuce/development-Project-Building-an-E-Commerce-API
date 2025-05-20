from flask import request, jsonify, Blueprint
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from marshmallow import ValidationError
from extensions import db
from database_models.order_table import OrderTable
from database_models.order_product_association_table import OrderProductAssociationTable
from database_models.product_table import ProductTable
from schema.order_schema import order_schema, orders_schema
from schema.product_schema import products_schema

order_blueprint = Blueprint('order_blueprint', __name__)

# POST /orders - Create a new order
@order_blueprint.route("/orders", methods=["POST"])
def create_order():
    if not request.is_json:
        return jsonify({"error": "Content-Type must be application/json"}), 415
    try:
        order_data = order_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400

    new_order = OrderTable(user_id=order_data["user_id"])
    db.session.add(new_order)
    db.session.commit()
    return order_schema.jsonify(new_order), 201

# PUT /orders/<order_id>/add_product/<product_id> - Add product to order
@order_blueprint.route("/orders/<int:order_id>/add_product/<int:product_id>", methods=["PUT"])
def add_product_to_order(order_id, product_id):
    exists = db.session.get(OrderTable, order_id)
    product = db.session.get(ProductTable, product_id)
    if not exists or not product:
        return jsonify({"error": "Order or Product not found"}), 404

    existing_assoc = db.session.get(OrderProductAssociationTable, (order_id, product_id))
    if existing_assoc:
        return jsonify({"error": "Product already in order"}), 400

    assoc = OrderProductAssociationTable(order_id=order_id, product_id=product_id)
    db.session.add(assoc)
    db.session.commit()
    return jsonify({"message": f"Product {product_id} added to order {order_id}"}), 200

# DELETE /orders/<order_id>/remove_product - Remove product from order
@order_blueprint.route("/orders/<int:order_id>/remove_product", methods=["DELETE"])
def remove_product_from_order(order_id):
    data = request.get_json()
    if not data or "product_id" not in data:
        return jsonify({"error": "Missing product_id in request body"}), 400

    product_id = data["product_id"]
    assoc = db.session.get(OrderProductAssociationTable, (order_id, product_id))
    if not assoc:
        return jsonify({"error": "Product not in order"}), 404

    db.session.delete(assoc)
    db.session.commit()
    return jsonify({"message": f"Product {product_id} removed from order {order_id}"}), 200

# GET /orders/user/<user_id> - Get all orders for a user
@order_blueprint.route("/orders/user/<int:user_id>", methods=["GET"])
def get_orders_by_user(user_id):
    orders = db.session.scalars(select(OrderTable).where(OrderTable.user_id == user_id)).all()
    if not orders:
        return jsonify({"error": "No orders found for this user"}), 404
    return orders_schema.jsonify(orders), 200

# GET /orders/<order_id>/products - Get all products for an order
@order_blueprint.route("/orders/<int:order_id>/products", methods=["GET"])
def get_products_for_order(order_id):
    assoc_products = db.session.scalars(
        select(ProductTable)
        .join(OrderProductAssociationTable, ProductTable.id == OrderProductAssociationTable.product_id)
        .where(OrderProductAssociationTable.order_id == order_id)
    ).all()

    if not assoc_products:
        return jsonify({"error": "No products found for this order"}), 404

    return products_schema.jsonify(assoc_products), 200
