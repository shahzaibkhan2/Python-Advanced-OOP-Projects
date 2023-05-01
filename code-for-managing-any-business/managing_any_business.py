# Defining a class for product
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    # Defining a function to format string
    def __str__(self):
        return f'{self.name} - Price: {self.price}, Quantity: {self.quantity}'


# Defining a class for order
class Order:
    def __init__(self, products, customer_name, customer_email):
        self.products = products
        self.customer_name = customer_name
        self.customer_email = customer_email
        self.total_price = sum(product.price * product.quantity for product in products)

    # Magic/Dunder method
    def __str__(self):
        return f'Order for {self.customer_name} ({self.customer_email}): {", ".join(product.name for product in self.products)}'


# Defining a class for business
class Business:
    def __init__(self, name):
        self.name = name
        self.products = []
        self.orders = []

    # Defining a function to add products
    def add_product(self, product):
        self.products.append(product)

    # Defining a function to add orders
    def add_order(self, order):
        self.orders.append(order)

    # Defining a function display products
    def display_products(self):
        for product in self.products:
            print(product)

    # Defining a function to display orders
    def display_orders(self):
        for order in self.orders:
            print(order)
