class Invoice:
    def __init__(self, order):
        self.order = order

    # Generates an invoice for the order    
    def generateInvoice(self):
        response = ''
        response += "Invoice for: " + self.order.customer.name + "\n"
        response += "Shipping to: " + self.order.shippingAddress + "\n"
        response += "Items:"+ "\n"
        for item in self.order.items:
            response += item.name + " $" + str(item.price)+ "\n"
        response += "Total: $" + str(self.order.total())+ "\n"
        response += "Payment Status: " + str(self.order.status)+ "\n"
        # # Writes the invoice to a text file in the 'orders' directory
        with open(f'orders/order_{self.order.orderID}.txt', 'a') as f:
            f.write(response)

        return response

