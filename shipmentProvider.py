class ShipmentProvider:
    # Constructor initializes shipments list and provider name.
    def __init__(self):
        self.shipments = []
        self.name = 'DHL'

    # Adds a shipment and sets its status to 'Preparing'.
    def addShipment(self, shipment):
        self.shipments.append(shipment)
        shipment.updateStatus('Preparing')

    # Updates a shipment's status. If status is 'Shipped', notifies the customer.
    def updateShipmentStatus(self, shipment, status):
        shipment.updateStatus(status)
        if status == 'Shipped':
            shipment.order.customer.notifyOrderShipped()


