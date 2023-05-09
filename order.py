class Order:
    def __init__(self, customer, items):
        self.customer = customer
        self.items = items
        self.shippingAddress = customer.address
        self.totalCost = 0
    def total(self):
        for item in self.items:
            self.totalCost += item.price
        return self.totalCost

    def update_history(self):
        # update order history...
        pass

