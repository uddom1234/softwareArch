from customer import Customer
from shoppingCart import ShoppingCart
from item import Item
from order import Order
from invoice import Invoice
from account import Account

customer = Customer("John Doe", "johndoe@example.com", "123 Main Street")
shoppingCart = ShoppingCart()

# Add items to the shopping cart
item1 = Item("Organic Apples", 5.99)
item2 = Item("Quinoa", 3.99)
shoppingCart.addItems(item1)
shoppingCart.addItems(item2)

# Place an order
order = Order(customer, shoppingCart.items)

# Generate invoice
invoice = Invoice(order)
invoiceDetails = invoice.generateInvoice()

# Create an account for the customer
account = Account(customer)
account.addToOrderHistory(order)
