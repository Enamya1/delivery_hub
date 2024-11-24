from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:1234@localhost/food_hub'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

# ----------------- Models -----------------
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    role = db.Column(db.Enum('customer', 'admin'), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.now())
    orders = db.relationship('Order', backref='user', cascade='all, delete-orphan')

class FoodCategory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    food_items = db.relationship('FoodItem', backref='category', cascade='all, delete-orphan')

class FoodItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Numeric(10, 2), nullable=False)
    image_url = db.Column(db.String(255))
    category_id = db.Column(db.Integer, db.ForeignKey('food_category.id'), nullable=False)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    total_amount = db.Column(db.Numeric(10, 2), nullable=False)
    status = db.Column(db.Enum('pending', 'completed', 'canceled'), default='pending')
    created_at = db.Column(db.DateTime, default=db.func.now())
    order_items = db.relationship('OrderItem', backref='order', cascade='all, delete-orphan')
    delivery = db.relationship('Delivery', backref='order', uselist=False, cascade='all, delete-orphan')

class OrderItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
    food_item_id = db.Column(db.Integer, db.ForeignKey('food_item.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Numeric(10, 2), nullable=False)

class Delivery(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
    delivery_address = db.Column(db.String(255), nullable=False)
    delivery_time = db.Column(db.DateTime)
    delivery_status = db.Column(db.Enum('pending', 'in_progress', 'delivered'), default='pending')
    worker_id = db.Column(db.Integer, db.ForeignKey('worker.id'))

class Worker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    vehicle_type = db.Column(db.String(50), nullable=False)
    status = db.Column(db.Enum('available', 'on_delivery'), default='available')
    deliveries = db.relationship('Delivery', backref='worker', cascade='all, delete-orphan')

# ----------------- Schemas -----------------
class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User

class FoodCategorySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = FoodCategory

class FoodItemSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = FoodItem

class OrderSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Order

class OrderItemSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = OrderItem

class DeliverySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Delivery

class WorkerSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Worker

user_schema = UserSchema()
users_schema = UserSchema(many=True)
category_schema = FoodCategorySchema()
categories_schema = FoodCategorySchema(many=True)
food_item_schema = FoodItemSchema()
food_items_schema = FoodItemSchema(many=True)
order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)
order_item_schema = OrderItemSchema()
order_items_schema = OrderItemSchema(many=True)
delivery_schema = DeliverySchema()
deliveries_schema = DeliverySchema(many=True)
worker_schema = WorkerSchema()
workers_schema = WorkerSchema(many=True)

# ----------------- API Endpoints -----------------
@app.route('/users', methods=['GET', 'POST'])
def manage_users():
    if request.method == 'GET':
        users = User.query.all()
        return jsonify(users_schema.dump(users))
    elif request.method == 'POST':
        data = request.get_json()
        new_user = User(
            username=data['username'],
            password=data['password'],
            email=data['email'],
            role=data['role']
        )
        db.session.add(new_user)
        db.session.commit()
        return jsonify(user_schema.dump(new_user)), 201

@app.route('/categories', methods=['GET', 'POST'])
def manage_categories():
    if request.method == 'GET':
        categories = FoodCategory.query.all()
        return jsonify(categories_schema.dump(categories))
    elif request.method == 'POST':
        data = request.get_json()
        new_category = FoodCategory(name=data['name'])
        db.session.add(new_category)
        db.session.commit()
        return jsonify(category_schema.dump(new_category)), 201

@app.route('/food_items', methods=['GET', 'POST'])
def manage_food_items():
    if request.method == 'GET':
        food_items = FoodItem.query.all()
        return jsonify(food_items_schema.dump(food_items))
    elif request.method == 'POST':
        data = request.get_json()
        new_food_item = FoodItem(
            name=data['name'],
            description=data['description'],
            price=data['price'],
            image_url=data.get('image_url'),
            category_id=data['category_id']
        )
        db.session.add(new_food_item)
        db.session.commit()
        return jsonify(food_item_schema.dump(new_food_item)), 201
@app.route('/tables', methods=['GET'])
def fetch_tables():
    try:
        # Test database connection
        db.session.execute('SELECT 1')

        workers = Worker.query.all()
        deliveries = Delivery.query.all()

        worker_data = [{"id": w.id, "name": w.name, "vehicle_type": w.vehicle_type, "status": w.status} for w in workers]
        delivery_data = [{"id": d.id, "pickup_address": d.pickup_address, "destination_address": d.destination_address, "delivery_status": d.delivery_status} for d in deliveries]

        return jsonify({"workers": worker_data, "deliveries": delivery_data}), 200
    except Exception as e:
        return jsonify({"error": "Database connection failed: " + str(e)}), 500


# ----------------- Initialize Database -----------------
with app.app_context():
    db.create_all()

# ----------------- Run Application -----------------
if __name__ == '__main__':
    app.run(debug=True)
