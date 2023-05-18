from shipmentProvider import ShipmentProvider
from shipment import Shipment
import random

class Order:
    def __init__(self, customer, items):
        self.shipment_provider = None
        self.orderStatus = "Pending"
        self.customer = customer
        self.items = items
        self.shippingAddress = customer.address
        self.totalCost = 0
        self.status = 'Pending Payment'
        self.orderID = random.randint(1, 1000)

    def total(self):
        for item in self.items:
            self.totalCost += float(item.price)
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
        self.status = oStatus

