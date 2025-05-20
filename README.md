# development-Project-Building-an-E-Commerce-API

## 🛒 Flask E-Commerce API

A RESTful API for a basic e-commerce system built with Flask, SQLAlchemy, and Marshmallow.

## 📦 Features

- Create, retrieve, update, and delete **Users** and **Products**
- Create **Orders** linked to Users
- Add/remove Products to/from Orders
- Fetch all orders for a specific User
- Fetch all Products in a specific Order
- Prevent duplicate products in a single order

## 🛠️ Technologies

- Python 3.11+
- Flask
- SQLAlchemy
- Marshmallow
- MySQL

## 📁 Project Structure

- ecommerce_api/
  - app.py
  - extensions.py
  - requirements.txt

  - database_models/
    - user_table.py
    - product_table.py
    - order_table.py
    - order_product_association_table.py

  - schema/
    - user_schema.py
    - product_schema.py
    - order_schema.py
    
  - endpoints/
    - user_endpoints.py
    - product_endpoints.py
    - order_endpoints.py


## Requirements

- backports-datetime-fromisoformat==2.0.3  
- blinker==1.9.0  
- click==8.2.0  
- Flask==3.1.1  
- flask-marshmallow==1.3.0  
- Flask-SQLAlchemy==3.1.1  
- greenlet==3.2.2  
- itsdangerous==2.2.0  
- Jinja2==3.1.6  
- MarkupSafe==3.0.2  
- marshmallow==4.0.0  
- marshmallow-sqlalchemy==1.4.2  
- mysql-connector-python==9.3.0  
- SQLAlchemy==2.0.41  
- typing_extensions==4.13.2  
- Werkzeug==3.1.3

all inside -requirements.txt