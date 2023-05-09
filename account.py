class Account:
    def __init__(self, customer):
        self.customer = customer
        self.orderHistory = []

    def addToOrderHistory(self, order):
        self.orderHistory.append(order)

    def requestPaymentMethod(self):
        # Display available payment methods to the customer
        print("Available payment methods:", self.customer.payment_methods)

        # Request payment method from the customer
        method = input("Please select a payment method: ")

        # Validate and set the selected payment method
        self.customer.select_payment_method(method)

        # Return the selected payment method
        return self.customer.select_payment_method







