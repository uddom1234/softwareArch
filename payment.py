from invoice import Invoice
class Payment:
    def __init__(self, order, account):
        self.order = order
        self.account = account
    
    # Processes a payment using a selected payment method
    def processPayment(self, paymentMethod):
        paymentMethods = ["Credit Card", "PayPal"]
        # Check if the selected method is valid
        paymentSuccessful = paymentMethod in paymentMethods


        if paymentSuccessful:
            print(f"Processing {paymentMethod} payment...")
            print("Payment successful !")
            invoice = Invoice(self.order)
            self.order.updateOrderStatus("Paid")
            return invoice.generateInvoice()

        else:
            self.order.updateOrderStatus("Pending")
            return "Payment failed !"
