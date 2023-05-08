class Account:
    def __init__(self, customer):
        self.customer = customer
        self.orderHistory = []

    def addToOrderHistory(self, order):
        self.orderHistory.append(order)








