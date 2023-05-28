class ShipmentProvider:
    def __init__(self):
        self.shipments = []

    def add_shipment(self, shipment):
        self.shipments.append(shipment)
        shipment.update_status('Preparing')

    def update_shipment_status(self, shipment, status):
        shipment.update_status(status)
        if status == 'Shipped':
            shipment.order.customer.notify_order_shipped()

