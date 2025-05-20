from password import password
from flask import Flask
from flask_marshmallow import Marshmallow
from sqlalchemy.orm import DeclarativeBase
from extensions import db, ma
from endpoints.user_endpoints import user_blueprint
from endpoints.product_endpoints import product_blueprint


#initialize the app
app = Flask(__name__)

#MySql data base config
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqlconnector://root:{password}@localhost/ecommerce_api'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#Creating base class
class Base(DeclarativeBase):
    pass

# Initialize extensions with app
db.init_app(app)
ma.init_app(app)

# Register blueprints
app.register_blueprint(user_blueprint)
app.register_blueprint(product_blueprint)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # create tables
    app.run(debug=True)