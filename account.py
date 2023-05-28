from orderManager import OrderManager

class Account:
    def __init__(self, customer, password, username):
        self.customer = customer
        self.password = password
        self.username = username
        self.orderHistory = []
        self.orderManager = OrderManager()

    def addToOrderHistory(self, order):
        self.orderHistory.append(order)
        with open(f'./orders/{self.username}_orders.txt', 'a') as f:
            f.write(f"Order: {order}\n")

    def requestPaymentMethod(self, method, order):
        return self.customer.selectPaymentMethod(method, order)

    def updatePaymentStatus(self, pStatus, order):
        if pStatus == "Success":
            self.paymentStatus = "Success"
            order.update_order_status("Paid")
            self.orderManager.confirmOrder(order)
        elif pStatus == "Failed":
            self.paymentStatus = "Failed"
            self.sendPaymentFailedMessage()

    def sendPaymentFailedMessage(self):
        message = "Payment failed!"
        print("Sending payment failed message to:", self.customer.email)
        print("Message:", message)
