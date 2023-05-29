import tkinter as tk
from orderManager import OrderManager

def shipmentPopup(Order):
    # Declare the shipment variable
    shipment = None

    # Define a function to confirm the order, add the shipment, write to a file, and close the window
    def confirm():
        # Create a shipment and add it
        shipment = orderManager.confirmOrder(Order)
        orderManager.shipmentProvider.addShipment(shipment)

        # Write shipment information to a file
        with open('shipments.txt', 'a') as file:
            file.write(f'Shipment Provider: {orderManager.shipmentProvider.name}, OrderID: {Order.orderID}, Shipping Address: {Order.shippingAddress}, Shipment Status: {shipment.status}\n')
        
        # Close the window
        window.destroy()

    # Create an instance of OrderManager
    orderManager = OrderManager()

    # Create a new tkinter window
    window = tk.Tk()
    window.title("Online Healthy Food Store")

    # Add a header to the window
    nameHeader = tk.Label(window, text="Your order has been shipped")
    nameHeader.grid(row=0, column=0)

    # Add an "Okay" button that runs the confirm function when clicked
    okBtn = tk.Button(window, text="Okay", command=confirm)
    okBtn.grid(row= 1, column= 0)

    # Start the tkinter event loop
    window.mainloop()
