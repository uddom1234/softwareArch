from shipment import Shipment
from shipmentProvider import ShipmentProvider

class OrderManager:
    # Constructor initializes the order manager with a shipment provider.
    def __init__(self):
        self.shipmentProvider = ShipmentProvider()

    # Confirms the order if it's paid, creates a new shipment, and returns it.
    def confirmOrder(self, order):
        if order.status != 'Paid':
            raise Exception("Order must be paid before it can be confirmed.")
        shipment = Shipment(order)
        return shipment
