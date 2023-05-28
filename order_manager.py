from shipment import Shipment
from shipmentProvider import ShipmentProvider

class OrderManager:
    def __init__(self):
        self.shipment_provider = ShipmentProvider()

    def confirm_order(self, order):
        if order.status != 'Paid':
            raise Exception("Order must be paid before it can be confirmed.")
        shipment = Shipment(order)
