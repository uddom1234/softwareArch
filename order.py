from shipment import Shipment
from shipmentProvider import ShipmentProvider


class Order:
    def __init__(self, customer, items):
        self.shipment_provider = None
        self.orderStatus = "Pending"
        self.customer = customer
        self.items = items
        self.shippingAddress = customer.address
        self.totalCost = 0
        self.status = 'Pending Payment'
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

    def updateOrderStatus(self, oStatus):
        if oStatus == "Paid":
            # Update order status to "Paid"
            self.orderStatus = "Paid"


        return self.totalCost

