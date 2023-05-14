class ShipmentProvider:
    def confirm_order(self, order):
        order.create_shipment()
        order.update_shipment_status("Assigned")
        self.deliver_shipment(order)

    def deliver_shipment(self, order):
        order.update_shipment_status("Delivered")
