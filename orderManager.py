from shipment import Shipment
from shipmentProvider import ShipmentProvider

class OrderManager:
    def __init__(self):
        self.shipmentProvider = ShipmentProvider()

    def confirmOrder(self, order):
        if order.status != 'Paid':
            raise Exception("Order must be paid before it can be confirmed.")
        shipment = Shipment(order)
        return shipment
