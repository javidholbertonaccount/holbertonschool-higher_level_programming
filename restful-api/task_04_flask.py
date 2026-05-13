#!/usr/bin/python3
"""
Task 04 Flask
"""
from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}

@app.route('/')
def home():
    """Home route"""
    return "Welcome to the Flask API!"

@app.route('/data')
def data():
    """Data route"""
    return jsonify(list(users.keys()))

@app.route('/status')
def status():
    """Status route"""
    return "OK"

@app.route('/users/<username>')
def get_user(username):
    """User route"""
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route('/add_user', methods=['POST'])
def add_user():
    """Add user route"""
    user_data = request.get_json()
    if not user_data:
        return jsonify({"error": "Invalid JSON"}), 400
    
    username = user_data.get('username')
    if not username:
        return jsonify({"error": "Username is required"}), 400
    
    if username in users:
        return jsonify({"error": "Username already exists"}), 409
    
    users[username] = user_data
    return jsonify({"message": "User added", "user": user_data}), 201

if __name__ == "__main__":
    app.run()
