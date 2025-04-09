from flask import  abort, request, Blueprint, jsonify, request
from fake_database import get_all_products, get_product_by_id, insert_product, delete_product, update_product
from product import Product

product_controller = Blueprint('product_controller', __name__)

@product_controller.route('/api/products', methods=['GET'])
def get_all():
    products = get_all_products()
    return jsonify([e.serialize() for e in products])

@product_controller.route('/api/products/<int:id>', methods=['GET'])
def get_id(id):
    product = get_product_by_id(id) # In the fake_database.py
    print(product)
    if product is None:
        abort(404, 'Product not found')
    return jsonify(product.serialize())

@product_controller.route('/api/products', methods = ['POST'])
def insert():
    data = request.json
    if len(data["name"]) == 0:
        abort(400, 'The name is mandatory')
    try:
        price = float(data["price"])
    except:
        abort(400, 'The price is mandatory')
    if price < 0:
        abort(400, 'The price must be positive')
    product = Product(0, data["name"], data["category"], price)
    product.id = insert_product(product)
    return jsonify(product.serialize())

@product_controller.route('/api/products/<int:id>', methods = ['PUT'])
def update(id):
    data = request.json
    if len(data['name']) == 0:
        abort(400, 'The name is mandatory')
    elif len(data['category']) == 0:
        abort(400, 'The category is mandatory')
    if 'price' not in data:
        abort(400, 'The price is mandatory')
    try:
        price = float(data['price'])
    except:
        abort(400, 'The price is not in a correct format')
    if price < 0:
        abort(400, 'The price must be positive')

    product = get_product_by_id(id)
    if product is None:
        abort(404, 'Product not found')
    result= update_product(product, data["name"], data["category"], price)
    return jsonify(result)

@product_controller.route('/api/products/<int:id>', methods = ['DELETE'])
def delete(id):
    product = get_product_by_id(id)
    if product is None:
        abort(404, 'Product not found')
    result=delete_product(id)
    return jsonify(result)
