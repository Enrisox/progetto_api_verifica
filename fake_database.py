from tkinter.font import names
from typing import List, Optional
from product import Product
from decimal import Decimal


# Fake database (list of products)
products_db: List[Product] = [
    Product(id=1,name="Laptop", category="Electronics", price=float("999.99")),
    Product(id=2,name="Smartphone", category="Electronics", price=float("499.99")),
    Product(id=3,name="Headphones", category="Accessories", price=float("79.99")),
    Product(id=4,name="Tablet", category="Electronics", price=float("299.99")),
    Product(id=5,name="Smartwatch", category="Wearables", price=float("199.99")),
    Product(id=6,name="Bluetooth Speaker", category="Audio", price=float("59.99")),
    Product(id=7,name="Gaming Mouse", category="Accessories", price=float("49.99")),
    Product(id=8,name="Mechanical Keyboard", category="Accessories", price=float("129.99")),
    Product(id=9,name="External SSD", category="Storage", price=float("149.99")),
    Product(id=10,name="4K Monitor", category="Displays", price=float("349.99")),
]

def get_all_products() -> List[Product]: # Return a list of products
    """Returns all products."""
    # products = []
    # for product in products_db:
    #     products.append(to_dict(product))
    # return products
    return products_db

def get_product_by_id(product_id: int) -> Optional[Product]:
    """Returns a product by its ID, or None if not found."""
    return next((p for p in products_db if p.id == product_id), None)

def insert_product(product: Product) -> None:
    """Inserts a new product into the database."""
    new_id = max((p.id for p in products_db), default=0) + 1 #auto-increment
    product.id = new_id
    products_db.append(product)
    return new_id

def update_product(product: Product, name: Optional[str] = None, category: Optional[str] = None, price: Optional[float] = None) -> bool:
    product.name=name
    product.category=category
    product.price=price
    return True

def delete_product(product_id: int) -> bool:
    """Deletes a product by ID. Returns True if successful, False if product not found."""
    global products_db
    product = get_product_by_id(product_id)
    if product:
        products_db = [p for p in products_db if p.id != product_id]
        return True
    return False

def to_dict(p):
    return {
        'id': p.id,
        'name': p.name,
        'category': p.category,
        'price': float(p.price)
    }