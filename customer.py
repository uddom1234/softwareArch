from account import Account
from payment import Payment
class Customer:
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address
        self.payment_methods = ["Credit Card", "PayPal"]
        self.selected_payment_method = None

    def select_payment_method(self, method):
        if method in self.payment_methods:
            Payment.processPayment(method)
        else:
            self.account.updatePaymentStatus(False)

    def signUp(self, username, password):
        self.account = Account(self, username, password)
        with open('accounts.txt', 'a') as f:
                    f.write(f"Name: {self.name}, Email: {self.email}, Username: {username}, Password: {password}, Address: {self.address}\n")




