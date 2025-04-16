from flask import Flask, jsonify, request

app = Flask(__name__)

#Simulate db in-memory
users = {}

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)

    if user:
        return jsonify({'id': user_id, 'name': user}), 200
    
    return jsonify({'error': 'User not found!'}), 404

@app.route('/users', methods=['POST'])
def add_user():
    data = request.json
    user_id = data.get('id')
    user_name = data.get('name')

    if not user_id or not user_name:
        return jsonify({ 'error': 'Invalid data'}), 400
    
    if user_id in users:
        return jsonify({ 'error': 'User exists'}), 400
    
    users[user_id] = user_name

    return jsonify({'id': user_id, 'name': user_name}), 200