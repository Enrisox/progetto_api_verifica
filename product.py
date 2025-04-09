
class Product:
    def __init__(self, id, name, category, price):
        if not isinstance(id, int):
            raise ValueError("The id has to be integer!!")
        if not isinstance(name, str):
            raise ValueError("The name has to be string!!")
        if not isinstance(category, str):
            raise ValueError("The category has to be string!!")
        if not isinstance(price, float):
            raise ValueError("The price has to be float!!")
        self.id=id
        self.name=name
        self.category=category
        self.price=price

    def __str__(self):
        string_to_return=f'ID: {self.id}, Name: {self.name}, Category {self.category}, Price: {self.price}'
        return string_to_return

    def serialize(self): #trasformation in json
        return {
            'id': self.id,
            'name': self.name,
            'category': self.category,
            'price': self.price
        }

