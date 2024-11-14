from flask import Flask, jsonify, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # For flash messages
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:1234@localhost/delivery-app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    # Method to check password
    def check_password(self, password):
        return check_password_hash(self.password, password)

    # Method to set password with hashing
    def set_password(self, password):
        self.password = generate_password_hash(password)

    def to_dict(self):
        # Convert User model to a dictionary that can be returned in API responses
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email
        }

# Route to handle signup
@app.route('/signup', methods=['POST'])
def signup():
    username = request.json.get('username')
    password = request.json.get('password')
    email = request.json.get('email')
    
    # Check if the username or email already exists
    if User.query.filter_by(username=username).first() or User.query.filter_by(email=email).first():
        return jsonify({'message': 'Username or Email already exists!'}), 400
    
    # Create a new user instance and hash the password
    new_user = User(username=username, email=email)
    new_user.set_password(password)

    # Add new user to the database
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'Account created successfully!'}), 201

# Route to handle login
@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    
    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        return jsonify({'message': 'Login successful!', 'user': user.to_dict()}), 200
    else:
        return jsonify({'message': 'Invalid credentials, please try again.'}), 401

# Route to get all users (API)
@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users]), 200

# Route to get a specific user by ID (API)
@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    user = User.query.get(id)
    if user:
        return jsonify(user.to_dict()), 200
    else:
        return jsonify({'message': 'User not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
