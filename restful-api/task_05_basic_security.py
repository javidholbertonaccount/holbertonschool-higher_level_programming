#!/usr/bin/python3
"""
Task 05 Basic Security
"""
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'super-secret-key'  # Change this in production
jwt = JWTManager(app)
auth = HTTPBasicAuth()

users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"}
}

@auth.verify_password
def verify_password(username, password):
    """Verify password for basic auth"""
    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        return username
    return None

@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    """Basic protected route"""
    return "Basic Auth: Access Granted"

@app.route('/login', methods=['POST'])
def login():
    """Login route to get JWT"""
    data = request.get_json()
    if not data:
        return jsonify({"error": "Missing JSON in request"}), 400
    
    username = data.get('username')
    password = data.get('password')
    
    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        access_token = create_access_token(identity={'username': username, 'role': user['role']})
        return jsonify(access_token=access_token)
    else:
        return jsonify({"error": "Invalid credentials"}), 401

@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    """JWT protected route"""
    return "JWT Auth: Access Granted"

@app.route('/admin-only')
@jwt_required()
def admin_only():
    """Admin only route"""
    current_user = get_jwt_identity()
    if current_user.get('role') == 'admin':
        return "Admin Access: Granted"
    else:
        return jsonify({"error": "Admin access required"}), 403

# Custom error handlers for JWT
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """Handle unauthorized error"""
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """Handle invalid token error"""
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(err):
    """Handle expired token error"""
    return jsonify({"error": "Token has expired"}), 401

@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    """Handle revoked token error"""
    return jsonify({"error": "Token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    """Handle needs fresh token error"""
    return jsonify({"error": "Fresh token required"}), 401

if __name__ == "__main__":
    app.run()
