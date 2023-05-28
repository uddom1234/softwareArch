from order_manager import OrderManager

class Account:
    def __init__(self, customer, password, username):
        self.customer = customer
        self.password = password
        self.username = username
        self.orderHistory = []
        self.order_manager = OrderManager()

    def addToOrderHistory(self, order):
        self.orderHistory.append(order)
        with open(f'./orders/{self.username}_orders.txt', 'a') as f:
            f.write(f"Order: {order}\n")

    def requestPaymentMethod(self):
        print("Available payment methods:", self.customer.payment_methods)
        method = input("Please select a payment method: ")
        self.customer.select_payment_method(method)
        return self.customer.select_payment_method

    def updatePaymentStatus(self, pStatus, order):
        if pStatus == "Success":
            self.paymentStatus = "Success"
            order.update_order_status("Paid")
            self.order_manager.confirm_order(order)
        elif pStatus == "Failed":
            self.paymentStatus = "Failed"
            self.sendPaymentFailedMessage()

    def sendPaymentFailedMessage(self):
        message = "Payment failed!"
        print("Sending payment failed message to:", self.customer.email)
        print("Message:", message)
