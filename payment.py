from invoice import Invoice
class Payment:
    def __init__(self, order, account):
        self.order = order
        self.account = account

    def processPayment(self, paymentMethod):
        paymentMethods = ["Credit Card", "PayPal"]
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