class Account:
    def __init__(self, customer, password, username):
        self.customer = customer
        self.password = password
        self.username = username
        self.orderHistory = []

    def addToOrderHistory(self, order):
        self.orderHistory.append(order)
        with open(f'./orders/{self.username}_orders.txt', 'a') as f:
            f.write(f"Order: {order}\n")








