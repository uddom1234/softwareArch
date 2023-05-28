class Shipment:
    def __init__(self, order):
        self.order = order
        self.status = 'New'

    def update_status(self, status):
        valid_statuses = ['New', 'Preparing', 'Shipped', 'Delivered']
        if status not in valid_statuses:
            raise Exception("Invalid shipment status.")
        self.status = status
