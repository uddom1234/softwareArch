import tkinter as tk
from orderManager import OrderManager

def shipmentPopup(Order):
    shipment = None

    def confirm():
        shipment = orderManager.confirmOrder(Order)
        orderManager.shipmentProvider.addShipment(shipment)
        with open('shipments.txt', 'a') as file:
            file.write(f'Shipment Provider: {orderManager.shipmentProvider.name}, OrderID: {Order.orderID}, Shipping Address: {Order.shippingAddress}, Shipment Status: {shipment.status}\n')
        window.destroy()

    orderManager = OrderManager()

    window = tk.Tk()
    window.title("Online Healthy Food Store")

    nameHeader = tk.Label(window, text="Your order has beeb shipped")
    nameHeader.grid(row=0, column=0)

    okBtn = tk.Button(window, text="Okay", command=confirm)
    okBtn.grid(row= 1, column= 0)


    window.mainloop()
