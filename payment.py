from invoice import Invoice
class Payment:
    def processPayment(self, paymentMethod):
        if paymentMethod == "Credit Card":
            # Process credit card payment
            print("Processing credit card payment...")
            paymentSuccessful = True
        elif paymentMethod == "PayPal":
            # Process PayPal payment
            print("Processing PayPal payment...")
            paymentSuccessful = True
        else:
            # Invalid payment method
            print("Invalid payment method")
            paymentSuccessful = False

        if paymentSuccessful:
            print("Payment successful")

            # Generate invoice
            invoice = Invoice(self.order)
            invoice.generateInvoice()

            # Update order status in Order class
            self.order.updateOrderStatus("Paid")

            # Update payment status in Account class
            self.account.updatePaymentStatus("Success")

        else:
            print("Payment failed")

            # Update order status in Order class
            self.order.updateOrderStatus("Pending")

            # Update payment status in Account class
            self.account.updatePaymentStatus("Failed")

