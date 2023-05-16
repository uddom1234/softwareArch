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

    def requestPaymentMethod(self):
        # Display available payment methods to the customer
        print("Available payment methods:", self.customer.payment_methods)

        # Request payment method from the customer
        method = input("Please select a payment method: ")

        # Validate and set the selected payment method
        self.customer.select_payment_method(method)

        # Return the selected payment method
        return self.customer.select_payment_method

    def updatePaymentStatus(self, pStatus):
        if pStatus == "Success":
            # Update payment status to "Success"
            self.paymentStatus = "Success"
        elif pStatus == "Failed":
            # Update payment status to "failed"
            self.paymentStatus = "Failed"
            # Send payment failed message to the customer
            self.sendPaymentFailedMessage()

    def sendPaymentFailedMessage(self):
        # Logic to send a payment failed message to the customer
        message = "Payment failed!"
        print("Sending payment failed message to:", self.customer.email)
        print("Message:", message)





