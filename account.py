class Account:
    def __init__(self, customer, username, password):
        self.customer = customer
        self.password = password
        self.username = username
        self.orderHistory = []

    def addToOrderHistory(self, order):
        self.orderHistory.append(order)
        with open(f'orders.txt', 'a') as f:
            f.write(f"Order: {order.orderID}, Total: {order.total()}, Status: {order.status}, Customer: {self.username}\n")

    def requestPaymentMethod(self, method, order):
        self.customer.selectPaymentMethod(method, order)