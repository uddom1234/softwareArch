class ShoppingCart:
    # Constructor function that initializes an empty list of items
    def __init__(self):
        self.items = []

    # Function to add an item to the list of items
    def addItems(self, item):
        self.items.append(item)

    # Function to remove an item from the list of items
    def deleteItems(self, item):
        self.items.remove(item)
    
    # Function to calculate the total cost of all items in the shopping cart
    def calculateTotalCost(self):
        totalCost = 0
        for item in self.items:
            totalCost += float(item.price)
        return totalCost



