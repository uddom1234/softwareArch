class Order:
    def __init__(self, customer, items):
        self.customer = customer
        self.items = items
        self.shippingAddress = customer.address

        