from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from models import db, User, Product, Order
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
jwt = JWTManager(app)

@app.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Check if the user already exists
    if User.query.filter_by(username=username).first():
        return jsonify({"msg": "User already exists!"}), 400

    # Create and save the new user
    user = User(username=username, password=password)
    db.session.add(user)
    db.session.commit()

    return jsonify({"msg": "User registered successfully!"}), 201

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Find the user by username
    user = User.query.filter_by(username=username).first()
    if not user or user.password != password:
        return jsonify({"msg": "Invalid credentials"}), 401

    # Create JWT token
    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)

@app.route('/api/products', methods=['GET'])
def get_products():
    # Get all products
    products = Product.query.all()
    return jsonify([{
        "id": p.id,
        "name": p.name,
        "description": p.description,
        "price": p.price
    } for p in products])

@app.route('/api/products/<int:id>', methods=['GET'])
def get_product(id):
    # Get a specific product by ID
    product = Product.query.get(id)
    if not product:
        return jsonify({"msg": "Product not found!"}), 404
    return jsonify({
        "id": product.id,
        "name": product.name,
        "description": product.description,
        "price": product.price
    })

@app.route('/api/orders', methods=['POST'])
@jwt_required()
def create_order():
    data = request.get_json()
    product_id = data.get('product_id')
    quantity = data.get('quantity')
    
    # Get the current logged-in user
    user_identity = request.jwt_identity
    user = User.query.filter_by(username=user_identity).first()

    if not user:
        return jsonify({"msg": "User not found"}), 404

    # Get the product
    product = Product.query.get(product_id)
    if not product:
        return jsonify({"msg": "Product not found"}), 404

    # Calculate total price
    total_price = product.price * quantity

    # Create the order
    order = Order(user_id=user.id, product_id=product.id, quantity=quantity, total_price=total_price)
    db.session.add(order)
    db.session.commit()

    return jsonify({"msg": "Order placed successfully!"}), 201

@app.route('/api/orders/<int:id>', methods=['GET'])
@jwt_required()
def get_order(id):
    # Get a specific order by ID
    order = Order.query.get(id)
    if not order:
        return jsonify({"msg": "Order not found!"}), 404
    return jsonify({
        "id": order.id,
        "user_id": order.user_id,
        "product_id": order.product_id,
        "quantity": order.quantity,
        "total_price": order.total_price
    })

if __name__ == '__main__':
    app.run(debug=True)
