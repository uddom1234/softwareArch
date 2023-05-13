class Order:
    def __init__(self, customer, items):
        self.customer = customer
        self.items = items
        self.shippingAddress = customer.address
        self.totalCost = 0
    def total(self):
        for item in self.items:
            self.totalCost += item.price
        return self.totalCost
    
     def confirm_order(self):
        self.shipment_provider = ShipmentProvider()
        self.shipment_provider.confirm_order(self)

    def create_shipment(self):
        self.shipment = Shipment()

    def update_shipment_status(self, status):
        self.shipment.update_status(status)

    def notify_customer(self):
        self.customer.notify_order_shipped()


