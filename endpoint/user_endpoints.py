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