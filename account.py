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

    def requestPaymentMethod(self, method):
        # Return the selected payment method
        return self.customer.select_payment_method(method)


    def updatePaymentStatus(self, pStatus):
        if pStatus:
            # Update payment status to "Success"
            self.paymentStatus = "Success"
            return 'Payment Successful'
        elif pStatus:
            # Update payment status to "failed"
            self.paymentStatus = "Failed"
            # Send payment failed message to the customer
            self.sendPaymentFailedMessage()

    def sendPaymentFailedMessage(self):
        # Logic to send a payment failed message to the customer
        message = "Payment failed!"
        return "Sending payment failed message to:", self.customer.email, "Message:", message





