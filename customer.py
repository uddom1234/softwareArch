from account import Account
class Customer:
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address
        self.account = None

    def signUp(self, username, password):
        self.account = Account(self, username, password)
        with open('accounts.txt', 'a') as f:
                    f.write(f"Name: {self.name}, Email: {self.email}, Username: {username}, Password: {password}, Address: {self.address}\n")



