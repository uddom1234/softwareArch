class Invoice:
    def __init__(self, order):
        self.order = order

    def generateInvoice(self):
        response = ''
        response += "Invoice for: " + self.order.customer.name + "\n"
        response += "Shipping to: " + self.order.shippingAddress + "\n"
        response += "Items:"+ "\n"
        for item in self.order.items:
            response += item.name + " $" + str(item.price)+ "\n"
        response += "Total: $" + str(self.order.total())+ "\n"
        response += "Payment Status: " + str(self.order.status)+ "\n"
        with open(f'orders/order_{self.order.orderID}.txt', 'a') as f:
            f.write(response)

        return response

