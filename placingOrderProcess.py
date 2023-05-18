import tkinter as tk
from shoppingCart import ShoppingCart
from item import Item
from order import Order
from invoice import Invoice
from paymentProcess import paymentProcess
def placingOrder(customer):
    # initiate the instance of shopping cart
    shoppingCart = ShoppingCart()
    #dictionary for storing old instances, because old instance != new instance even though name and stuff is the same
    itemDic = {}

    def addToCart(event):
        if listOfItems.curselection():
            #dissect the item price and name from the list. then fetching the instance stored in the itemDic
            selected_item = listOfItems.get(listOfItems.curselection())
            itemName, itemPrice = selected_item.split(' - $')
            item = itemDic[itemName]
            
            #using our shoppingCart class method addItems
            shoppingCart.addItems(item)
            refreshCart()

    def removeItem():
        if cartItems.curselection():
            #dissect the item price and name from the list. then fetching the instance stored in the itemDic
            selected_item = cartItems.get(cartItems.curselection())
            itemName, itemPrice = selected_item.split(' - $')
            item = itemDic[itemName]

            #using our shoppingCart class method removeItem to remove the item from the list
            shoppingCart.deleteItems(item)
            refreshCart()

    def refreshCart():
        #everytime this is called, we empty the list from the tkinter section, then we looop through the shoppingCart.items and add it back
        #doing this ensures that it will not generate more stuff on top of the existing items in the tkinter
        cartItems.delete(0, tk.END)
        for item in shoppingCart.items:
            cartItems.insert(tk.END, f"{item.name} - ${item.price}")

    def placeOrder():
        order = Order(customer, shoppingCart.items)
        customer.account.addToOrderHistory(order)
        result.set(f"Order placed and added to order history. Total cost: ${shoppingCart.calculateTotalCost()}")
        window.destroy()
        paymentProcess(customer)
        refreshCart()

    window = tk.Tk()
    window.title("Online Healthy Food Store")

    # creating the area for displaying the items
    listOfItems = tk.Listbox(window)
    listOfItems.grid(row=0, column=0)
    listOfItems.bind('<<ListboxSelect>>', addToCart)

    #goes through the items.txt file and list all the items
    with open('items.txt', 'r') as file:
        for line in file:
            #the text file is structured like a dict: Name: {name}, Price: {price}
            #it is seperated with a space and comma
            #this will remove any empty space infront or behind each row then split each items by ', '
            itemInfo = line.strip().split(', ')

            #individual items are split again and put into dictionary for each items: Name, then goes to Price
            itemInfo = {info.split(': ')[0]: info.split(': ')[1] for info in itemInfo}

            #the information is then taken as params for the item constructor
            item = Item(itemInfo['Name'], itemInfo['Price'])
            itemDic[item.name] = item

            #it adds all the items into the item lists
            listOfItems.insert(tk.END, f"{item.name} - ${item.price}")

    #stuff in shopping cart
    cartHeader = tk.Label(window, text="Shopping Cart Contents:")
    cartHeader.grid(row=1, column=0)
    cartItems = tk.Listbox(window, width=30, height=10)
    cartItems.grid(row=2, column=0)

    removeItemBtn = tk.Button(window, text="Delete Selected Item", command=removeItem)
    removeItemBtn.grid(row=3, column=0)

    placeOrderBtn = tk.Button(window, text="Place Order", command=placeOrder)
    placeOrderBtn.grid(row=4, column=0)

    result = tk.StringVar()
    resultHeader = tk.Label(window, textvariable=result)
    resultHeader.grid(row=5, column=0)

    window.mainloop()
