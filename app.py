from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import mysql.connector

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://username:password@localhost/delivry-app'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Worker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    vehicle_type = db.Column(db.String(255), nullable=False)
    status = db.Column(db.String(50), nullable=False)
    last_known_latitude = db.Column(db.Float, nullable=False)
    last_known_longitude = db.Column(db.Float, nullable=False)

class Delivery(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    worker_id = db.Column(db.Integer, db.ForeignKey('worker.id'))
    pickup_address = db.Column(db.String(255), nullable=False)
    destination_address = db.Column(db.String(255), nullable=False)
    delivery_status = db.Column(db.String(50), nullable=False)
    pickup_time = db.Column(db.DateTime)
    delivery_time = db.Column(db.DateTime)

# Create database tables
with app.app_context():
    db.create_all()

@app.route('/workers', methods=['GET', 'POST'])
def manage_workers():
    if request.method == 'GET':
        workers = Worker.query.all()
        return jsonify([worker.name for worker in workers]), 200

    if request.method == 'POST':
        data = request.get_json()
        new_worker = Worker(
            name=data['name'],
            vehicle_type=data['vehicle_type'],
            status=data['status'],
            last_known_latitude=data['last_known_latitude'],
            last_known_longitude=data['last_known_longitude']
        )
        db.session.add(new_worker)
        db.session.commit()
        return jsonify({"message": "Worker added successfully"}), 201

@app.route('/workers/<int:id>', methods=['PUT'])
def update_worker(id):
    data = request.get_json()
    worker = Worker.query.get(id)
    if worker:
        worker.status = data.get('status', worker.status)
        worker.last_known_latitude = data.get('last_known_latitude', worker.last_known_latitude)
        worker.last_known_longitude = data.get('last_known_longitude', worker.last_known_longitude)
        db.session.commit()
        return jsonify({"message": "Worker updated successfully"}), 200
    return jsonify({"message": "Worker not found"}), 404

@app.route('/deliveries', methods=['GET', 'POST'])
def manage_deliveries():
    if request.method == 'GET':
        deliveries = Delivery.query.all()
        return jsonify([{
            'pickup_address': delivery.pickup_address,
            'destination_address': delivery.destination_address,
            'status': delivery.delivery_status
        } for delivery in deliveries]), 200

    if request.method == 'POST':
        data = request.get_json()
        new_delivery = Delivery(
            worker_id=data['worker_id'],
            pickup_address=data['pickup_address'],
            destination_address=data['destination_address'],
            delivery_status=data['delivery_status'],
            pickup_time=data['pickup_time'],
            delivery_time=data['delivery_time']
        )
        db.session.add(new_delivery)
        db.session.commit()
        return jsonify({"message": "Delivery created successfully"}), 201

@app.route('/deliveries/<int:id>', methods=['PUT'])
def update_delivery(id):
    data = request.get_json()
    delivery = Delivery.query.get(id)
    if delivery:
        delivery.delivery_status = data.get('delivery_status', delivery.delivery_status)
        db.session.commit()
        return jsonify({"message": "Delivery updated successfully"}), 200
    return jsonify({"message": "Delivery not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
