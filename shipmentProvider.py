class ShipmentProvider:
    def __init__(self):
        self.shipments = []
        self.name = 'DHL'

    def addShipment(self, shipment):
        self.shipments.append(shipment)
        shipment.updateStatus('Preparing')

    def updateShipmentStatus(self, shipment, status):
        shipment.updateStatus(status)
        if status == 'Shipped':
            shipment.order.customer.notifyOrderShipped()

