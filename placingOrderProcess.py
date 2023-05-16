import tkinter as tk
from customer import Customer
from shoppingCart import ShoppingCart
from item import Item
from order import Order
from invoice import Invoice
from account import Account

def placingOrder(customer):
    def add_item():
        item_name = item_name_entry.get()
        item_price = float(item_price_entry.get())
        item = Item(item_name, item_price)
        shoppingCart.addItems(item)
        update_cart()

    def remove_item():
        item_index = int(item_index_entry.get())
        shoppingCart.removeItems(item_index)
        update_cart()

    def place_order():
        order = Order(customer, shoppingCart.items)
        invoice = Invoice(order)
        invoiceDetails = invoice.generateInvoice()
        customer.account.addToOrderHistory(order)
        result.set("Order placed and added to order history")
        update_cart()

    def update_cart():
        cart_contents.delete(1.0, tk.END)
        for item in shoppingCart.items:
            cart_contents.insert(tk.END, f"{item.name} - ${item.price}\n")

    # Initialize shopping cart
    shoppingCart = ShoppingCart()

    # Create the main window
    window = tk.Tk()
    window.title("Online Healthy Food Store")

    # Create labels, entries, and buttons for adding items
    item_name_label = tk.Label(window, text="Item Name:")
    item_name_label.grid(row=11, column=0)
    item_name_entry = tk.Entry(window)
    item_name_entry.grid(row=11, column=1)

    item_price_label = tk.Label(window, text="Item Price:")
    item_price_label.grid(row=12, column=0)
    item_price_entry = tk.Entry(window)
    item_price_entry.grid(row=13, column=1)

    add_item_button = tk.Button(window, text="Add Item", command=add_item)
    add_item_button.grid(row=14, column=0)

    # Create labels, entries, and buttons for removing items
    item_index_label = tk.Label(window, text="Item Index to Remove:")
    item_index_label.grid(row=15, column=0)
    item_index_entry = tk.Entry(window)
    item_index_entry.grid(row=9, column=1)

    remove_item_button = tk.Button(window, text="Remove Item", command=remove_item)
    remove_item_button.grid(row=10, column=0)

    # Create button for placing an order
    place_order_button = tk.Button(window, text="Place Order", command=place_order)
    place_order_button.grid(row=11, column=0)

    # Create a label for displaying the result
    result = tk.StringVar()
    result_label = tk.Label(window, textvariable=result)
    result_label.grid(row=11, column=1)

    # Create a text widget for displaying the shopping cart contents
    cart_label = tk.Label(window, text="Shopping Cart Contents:")
    cart_label.grid(row=12, column=0)
    cart_contents = tk.Text(window, width=30, height=10)
    cart_contents.grid(row=13, column=0)

    # Run the application
    window.mainloop()
