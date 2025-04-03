'''from flask import Flask, render_template,abort, request
app = Flask (__name__)
@app.route("/")
def homepage():
    return render_template("index.html")

@app.route()

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5000)'''

from flask import Flask, render_template, abort, jsonify, request
from fake_database import get_all_products, get_product_by_id, insert_product
from product import Product

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/api/products", methods=["GET"])
def get_all():
    products = get_all_products()
    return jsonify(products)

@app.route("/api/product/<int:id>", methods=["GET"])
def get_by_id(id):
    product = get_product_by_id(id)
    if product is None:
        abort(404, description="Product not found")
    return jsonify(product)

@app.route("/api/products", methods=["POST"])
def add_product():
    data = request.get_json()

    # Verifica che i dati richiesti siano presenti
    if not data or 'name' not in data or 'category' not in data or 'price' not in data:
        abort(400, description="Missing required fields: 'name', 'category', 'price'")

    # Crea un nuovo prodotto e lo inserisce nel database
    new_product = Product(name=data['name'], category=data['category'], price=data['price'])
    insert_product(new_product)

    return jsonify(to_dict(new_product)), 201  # Restituisce il prodotto appena aggiunto

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

