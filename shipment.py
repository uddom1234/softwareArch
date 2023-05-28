class Shipment:
    def __init__(self, order):
        self.order = order
        self.status = 'New'

    def updateStatus(self, status):
        validStatuses = ['New', 'Preparing', 'Shipped', 'Delivered']
        if status not in validStatuses:
            raise Exception("Invalid shipment status.")
        self.status = status
