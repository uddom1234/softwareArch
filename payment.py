class Payment:
    def __init__(self, order):
        self.order = order

    def processPayment(self, paymentMethod):
        if paymentMethod == "credit":
            # Process credit card payment
            print("Processing credit card payment...")
            payment_successful = True
        elif paymentMethod == "paypal":
            # Process PayPal payment
            print("Processing PayPal payment...")
            payment_successful = True
        else:
            # Invalid payment method
            print("Invalid payment method")
            payment_successful = False

        if payment_successful:
            print("Payment successful")
            # Generate invoice
            invoice = Invoice(self.order)
            invoice.generateInvoice()
            # Update payment status in Account class
            self.account.updatePaymentStatus("paid")
        else:
            print("Payment failed")
            # Update payment status in Account class
            self.account.updatePaymentStatus("failed")

