from account import Account
class Customer:
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address
        self.payment_methods = ["Credit Card", "PayPal"]
        self.selected_payment_method = None

    def select_payment_method(self, method):
        if method in self.payment_methods:
            self.selected_payment_method = method
            print("Selected payment method:", method)
        else:
            print("Invalid payment method")

        self.account = None

    def signUp(self, username, password):
        self.account = Account(self, username, password)
        with open('accounts.txt', 'a') as f:
                    f.write(f"Name: {self.name}, Email: {self.email}, Username: {username}, Password: {password}, Address: {self.address}\n")




