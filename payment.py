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
            invoice.generateInvoice()

        else:
            print("Payment failed !")

        self.updateOrderStatus(paymentSuccessful)

    def updateOrderStatus(self, success):
        orderStatus = "Paid" if success else "Pending"

        # Update order status in Order class
        self.order.updateOrderStatus(orderStatus)