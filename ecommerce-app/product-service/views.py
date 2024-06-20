from flask import request, jsonify
from sqlalchemy.exc import StaleDataError
from app import app, db
from models import Product

@app.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify([{'id': p.id, 'name': p.name, 'quantity': p.quantity, 'price': p.price} for p in products])

@app.route('/products', methods=['POST'])
def add_product():
    data = request.json
    new_product = Product(name=data['name'], quantity=data['quantity'], price=data['price'])
    db.session.add(new_product)
    db.session.commit()
    return jsonify({'message': 'Product added successfully'}), 201

@app.route('/products/<int:id>', methods=['PUT'])
def update_product(id):
    data = request.json
    product = Product.query.get_or_404(id)
    try:
        product.name = data['name']
        product.quantity = data['quantity']
        product.price = data['price']
        db.session.commit()
        return jsonify({'message': 'Product updated successfully'}), 200
    except StaleDataError:
        db.session.rollback()
        return jsonify({'message': 'Conflict detected, please retry'}), 409
