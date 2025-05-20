from extensions import db
from database_models.user_table import User
from schema.user_schema import user_schema, users_schema
from sqlalchemy import select
from flask import request, jsonify, Blueprint
from marshmallow import ValidationError


user_blueprint = Blueprint('user_blueprint', __name__)

#create User
@user_blueprint.route("/users", methods=["POST"])
def create_user():
    if not request.is_json:
        return jsonify({"error": "Content-Type must be application/json"}), 415

    try:
        user_data = user_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400
    
    new_user = User(name=user_data['name'], email=user_data['email'], address=user_data['address'])
    db.session.add(new_user)
    db.session.commit()
    
    return user_schema.jsonify(new_user), 201


#Read users
@user_blueprint.route("/users", methods=["GET"])
def read_user():
    users = db.session.scalars(select(User)).all()
    if not users:
        return jsonify({"error": "No users found"}), 404
    
    return users_schema.jsonify(users)

#Read user by ID
@user_blueprint.route("/users/<int:id>", methods=["GET"])
def read_user_id(id):
    
    user = db.session.get(User, id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    
    return  user_schema.jsonify(user)


#Update user
@user_blueprint.route("/users/<int:id>", methods=["PUT"])
def update_user(id):
    
    user = db.session.get(User, id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    
    try:
        user_data = user_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400
    
    user.name = user_data["name"]
    user.email = user_data["email"]
    user.address = user_data["address"]
    
    db.session.commit()
    return user_schema.jsonify(user), 200


#Delete User
@user_blueprint.route("/users/<int:id>", methods=["DELETE"])
def delete_user(id):
    user = db.session.get(User, id)
    
    if not user:
        return jsonify({"error": "Invalid user id"}), 400
    
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": f"Successfully deleted user {id}"}), 200