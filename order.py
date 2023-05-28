from customer import Customer
class Order:
    def __init__(self, customer, items):
        self.customer = customer
        self.items = items
        self.shippingAddress = customer.address
        self.totalCost = 0
        self.status = 'Pending Payment'

    def total(self):
        for item in self.items:
            self.totalCost += item.price
        return self.totalCost

    def update_order_status(self, oStatus):
        if oStatus == "Paid":
            self.status = "Paid"
        elif oStatus == "Pending":
            self.status = "Pending"
        else:
            raise Exception("Invalid order status.")
        return self.totalCost
