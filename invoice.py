class Invoice:
    def __init__(self, order):
        self.order = order

    def generateInvoice(self):
        print("Invoice for: " + self.order.customer.name)
        print("Shipping to: " + self.order.shippingAddress)
        print("Items:")
        for item in self.order.items:
            print(item.name + " $" + str(item.price))
        print("Total: $" + str(self.order.total()))