from flask import Flask, render_template, abort, request
from product import Product
import json as js
from product_controller import product_controller
from flask_cors import CORS

app =Flask(__name__)
app.register_blueprint(product_controller)

CORS(app)

@app.route("/")
def homepage():
    return render_template('index.html')

@app.route("/", methods = ['POST'])
def homepage_post():
    return "POST route"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

