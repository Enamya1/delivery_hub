from flask import Flask, jsonify, request
import mysql.connector
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This is to allow cross-origin requests from your frontend

# Database connection setup
def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='1234',
        database='delivery-app'
    )

# Route to add a worker
@app.route('/worker', methods=['POST'])
def add_worker():
    data = request.get_json()

    name = data['name']
    status = data['status']

    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            '''INSERT INTO delivery_workers (name, status) 
               VALUES (%s, %s)''', (name, status)
        )
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({'message': 'Worker added successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Route to get all workers
@app.route('/workers', methods=['GET'])
def get_workers():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM delivery_workers")
        workers = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(workers), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Route to update a worker's status
@app.route('/update-worker', methods=['POST'])
def update_worker():
    data = request.get_json()
    
    worker_id = data['id']
    status = data['status']
    
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            '''UPDATE delivery_workers 
               SET status = %s 
               WHERE id = %s''', (status, worker_id)
        )
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({'message': 'Worker updated successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Route to track a specific worker by ID
@app.route('/track-worker/<worker_id>', methods=['GET'])
def track_worker(worker_id):
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM delivery_workers WHERE id = %s", (worker_id,))
        worker = cursor.fetchone()
        cursor.close()
        conn.close()
        if worker:
            return jsonify(worker), 200
        else:
            return jsonify({'message': 'Worker not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
