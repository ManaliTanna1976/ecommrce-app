from flask import request, jsonify
from app import app, db
from models import Order
from flask_jwt_extended import jwt_required, get_jwt_identity

@app.route('/orders', methods=['POST'])
@jwt_required()
def create_order():
    data = request.json
    user_id = get_jwt_identity()
    new_order = Order(user_id=user_id, product_id=data['product_id'], quantity=data['quantity'])
    db.session.add(new_order)
    db.session.commit()
    return jsonify({'message': 'Order created successfully'}), 201

@app.route('/orders', methods=['GET'])
@jwt_required()
def get_orders():
    user_id = get_jwt_identity()
    orders = Order.query.filter_by(user_id=user_id).all()
    return jsonify([{'id': o.id, 'product_id': o.product_id, 'quantity': o.quantity, 'status': o.status} for o in orders])
