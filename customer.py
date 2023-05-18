from account import Account
from payment import Payment
class Customer:
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address
        self.payment_methods = ["Credit Card", "PayPal"]
        self.selected_payment_method = None

    def selectPaymentMethod(self, method, order):
        if method in self.payment_methods:
            # Creating a new instance of Payment class
            # Passing the order and account to the Payment object
            payment = Payment(order, self.account)
            return payment.processPayment(method)
        else:
            return "Invalid payment method."

    def signUp(self, username, password):
        self.account = Account(self, username, password)
        with open('accounts.txt', 'a') as f:
                    f.write(f"Name: {self.name}, Email: {self.email}, Username: {username}, Password: {password}, Address: {self.address}\n")




