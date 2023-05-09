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

