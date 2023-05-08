class Payment:
    def __init__(self, order):
        self.order = order

    def makePayment(self, paymentInfo):
        # process payment
        paymentGateway = PaymentGateway()
        paymentStatus = paymentGateway.processPayment(paymentInfo, self.order.total())

        if paymentStatus == "success":
            # generate invoice
            invoice = Invoice(self.order)
            invoice.generateInvoice()

            return "Payment successful. Thank you for shopping with us!"
        else:
            return "Payment failed. Your order have been cancelled."
