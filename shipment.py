class Shipment:
    # Constructor initializes the shipment with an order and sets its status to 'New'.
    def __init__(self, order):
        self.order = order
        self.status = 'New'

    # Updates the shipment status if it's valid, otherwise raises an exception.
    def updateStatus(self, status):
        validStatuses = ['New', 'Preparing', 'Shipped', 'Delivered']
        if status not in validStatuses:
            raise Exception("Invalid shipment status.")
        self.status = status
