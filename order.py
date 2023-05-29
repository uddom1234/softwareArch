from customer import Customer
import random

class Order:
    def __init__(self, customer, items):
        self.customer = customer
        self.items = items
        self.shippingAddress = customer.address
        self.totalCost = 0
        self.status = 'Pending Payment'
        self.orderID = random.randint(1, 1000)
    
    # Calculates the total cost of the items
    def total(self):
        for item in self.items:
            self.totalCost += float(item.price)
        return self.totalCost

    # Updates the order status based on the input argument
    def updateOrderStatus(self, oStatus):
        if oStatus == "Paid":
            self.status = "Paid"
        elif oStatus == "Pending":
            self.status = "Pending"
        else:
            raise Exception("Invalid order status.")
        return self.totalCost
