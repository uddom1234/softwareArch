import tkinter as tk
from shoppingCart import ShoppingCart
from item import Item
from order import Order
from invoice import Invoice

def placingOrder(customer):
    # Initialize shopping cart
    shoppingCart = ShoppingCart()
    #dictionary for storing old instances, because old instance != new instance even though name and stuff is the same
    itemDic = {}

    def addToCart(event):
        if listOfItems.curselection():  # add this line
            #dissect the item price and name from the list. then fetching the instance stored in the itemDic
            selected_item = listOfItems.get(listOfItems.curselection())
            itemName, itemPrice = selected_item.split(' - $')
            item = itemDic[itemName]
            
            #using our shoppingCart class method addItems
            shoppingCart.addItems(item)
            refreshCart()

    def removeItem():
        if cart_contents.curselection():  # add this line
            selected_item = cart_contents.get(cart_contents.curselection())
            itemName, itemPrice = selected_item.split(' - $')
            item = itemDic[itemName]
            shoppingCart.deleteItems(item)
            refreshCart()

    def refreshCart():
        cart_contents.delete(0, tk.END)
        for item in shoppingCart.items:
            cart_contents.insert(tk.END, f"{item.name} - ${item.price}")

    def place_order():
        order = Order(customer, shoppingCart.items)
        invoice = Invoice(order)
        invoiceDetails = invoice.generateInvoice()
        customer.account.addToOrderHistory(order)
        result.set(f"Order placed and added to order history. Total cost: ${shoppingCart.calculateTotalCost()}")
        refreshCart()

    # Create the main window
    window = tk.Tk()
    window.title("Online Healthy Food Store")

    # Create a ListBox for item list
    listOfItems = tk.Listbox(window)
    listOfItems.grid(row=0, column=0)
    listOfItems.bind('<<ListboxSelect>>', addToCart)


    #goes through the items.txt file and list all the items
    with open('items.txt', 'r') as file:
        for line in file:
            itemInfo = line.strip().split(', ')
            itemInfo = {info.split(': ')[0]: info.split(': ')[1] for info in itemInfo}
            item = Item(itemInfo['Name'], itemInfo['Price'])
            itemDic[item.name] = item
            listOfItems.insert(tk.END, f"{item.name} - ${item.price}")

    # Create a ListBox for displaying the shopping cart contents
    cart_label = tk.Label(window, text="Shopping Cart Contents:")
    cart_label.grid(row=1, column=0)
    cart_contents = tk.Listbox(window, width=30, height=10)
    cart_contents.grid(row=2, column=0)

    # Create button for deleting an item from the cart
    delete_item_button = tk.Button(window, text="Delete Selected Item", command=removeItem)
    delete_item_button.grid(row=3, column=0)

    # Create button for placing an order
    place_order_button = tk.Button(window, text="Place Order", command=place_order)
    place_order_button.grid(row=4, column=0)

    # Create a label for displaying the result
    result = tk.StringVar()
    result_label = tk.Label(window, textvariable=result)
    result_label.grid(row=5, column=0)

    # Run the application
    window.mainloop()
