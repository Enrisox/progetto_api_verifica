from decimal import Decimal

class Product:
    def __init__(self, id: int, name: str, category: str, price: Decimal):
        self.id = id
        self.name = name
        self.category = category
        self.price = price

    def __repr__(self):
        return f"Product(id={self.id}, name='{self.name}', category='{self.category}', price={self.price})"

    def serialize(self):
            return {
                'id': self.id, 
                'name': self.name,
                'category': self.category,
                'price': self.price
            }    