from typing import List, Optional
from decimal import Decimal
from product import Product

# Fake database (list of products)
products_db: List[Product] = [
    Product(name="Laptop", category="Electronics", price=999.99),
    Product(name="Smartphone", category="Electronics", price=499.99),
    Product(name="Headphones", category="Accessories", price=79.99),
    Product(name="Tablet", category="Electronics", price=299.99),
    Product(name="Smartwatch", category="Wearables", price=199.99),
    Product(name="Bluetooth Speaker", category="Audio", price=59.99),
    Product(name="Gaming Mouse", category="Accessories", price=49.99),
    Product(name="Mechanical Keyboard", category="Accessories", price=129.99),
    Product(name="External SSD", category="Storage", price=149.99),
    Product(name="4K Monitor", category="Displays", price=349.99),
]

def get_all_products():
    """Returns all products as a list of dictionaries."""
    return [to_dict(product) for product in products_db]

def get_product_by_id(product_id: int) -> Optional[Product]:
    """Returns a product by its ID, or None if not found."""
    return next((to_dict(p) for p in products_db if p.id == product_id), None)

def insert_product(product: Product) -> None:
    """Inserts a new product into the database."""
    products_db.append(product)

def update_product(product_id: int, name: Optional[str] = None, category: Optional[str] = None, price: Optional[Decimal] = None) -> bool:
    """Updates an existing product. Returns True if successful, False if product not found."""
    product = get_product_by_id(product_id)
    if product:
        if name is not None:
            product.name = name
        if category is not None:
            product.category = category
        if price is not None:
            product.price = price
        return True
    return False

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
