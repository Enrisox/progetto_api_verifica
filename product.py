'''class Product:
    def __init__(self,id,name,category, price):
        if not isinstance(id, int):
            raise ValueError("error, deve essere un intero")
        if not isinstance(name, str):
            raise ValueError("error, deve essere una stringa")
        if not isinstance(category, str):
            raise ValueError("error, deve essere una stringa")
        if not isinstance(price, int):
            raise ValueError("error, deve essere un intero")

        self.id = id
        self.name = name
        self.category = category
        self.price = price

    def __str__(self):
        return f"Product(product_id={self.id}, name={self.name}, category={self.category}, price={self.price})"'''
# product.py

class Product:
    _id_counter = 1  # Variabile di classe per generare ID univoci

    def __init__(self, name, category, price, product_id=None):
        if product_id is None:
            self.id = Product._id_counter
            Product._id_counter += 1
        else:
            self.id = product_id
        self.name = name
        self.category = category
        self.price = price
