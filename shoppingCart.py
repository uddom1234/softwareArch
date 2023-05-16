class ShoppingCart:
    def __init__(self):
        self.items = []

    def addItems(self, item):
        self.items.append(item)

    def deleteItems(self, item):
        self.items.remove(item)
    def calculateTotalCost(self):
        totalCost = 0
        for item in self.items:
            totalCost += item.price
        return totalCost



