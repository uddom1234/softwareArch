import tkinter as tk
from account import Account
from customer import Customer
from placingOrderProcess import placingOrder
def sessionAccount():
    global customer
    name = name_entry.get()
    email = email_entry.get()
    address = address_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    try:
        with open(f'accounts.txt', 'r') as file:
            for line in file:
                account_info = line.strip().split(', ')
                account_dict = {info.split(': ')[0]: info.split(': ')[1] for info in account_info}
                userEmail = account_dict['Username']
                userPassword = account_dict['Password']

                if userEmail == username and userPassword == password:
                    customer = Customer(account_dict['Name'], account_dict['Email'], account_dict['Address'])
                    customer.account = Account(customer, username, password)
                    result.set(f"Signed in, Welcome {customer.name}!")
                    currentAccount = customer.account
                    window.destroy()

                elif userEmail == username and userPassword != password:
                    result.set("Incorrect password")

                else:
                    customer = Customer(name, email, address)
                    customer.signUp(username, password)
                    currentAccount = customer.account
                    result.set(f"Account created for {name}")
    except FileNotFoundError:
        customer = Customer(name, email, address)
        customer.signUp(username, password)
        currentAccount = customer.account
        result.set(f"Account created for {name}")

    if(customer):
        placingOrder(customer)

# Create the main window
window = tk.Tk()
window.title("Online Healthy Food Store")

# Create labels, entries, and buttons for creating an account
name_label = tk.Label(window, text="Name:")
name_label.grid(row=0, column=0)
name_entry = tk.Entry(window)
name_entry.grid(row=1, column=0)

email_label = tk.Label(window, text="Email:")
email_label.grid(row=0, column=1)
email_entry = tk.Entry(window)
email_entry.grid(row=1, column=1)

address_label = tk.Label(window, text="Address:")
address_label.grid(row=0, column=2)
address_entry = tk.Entry(window)
address_entry.grid(row=1, column=2)

username_label = tk.Label(window, text="Username:")
username_label.grid(row=2, column=0)
username_entry = tk.Entry(window)
username_entry.grid(row=3, column=0)

password_label = tk.Label(window, text="Password:")
password_label.grid(row=2, column=1)
password_entry = tk.Entry(window, show='*')
password_entry.grid(row=3, column=1)

create_account_button = tk.Button(window, text="Create Account", command=sessionAccount)
create_account_button.grid(row=4, column=1)

# Create a label for displaying the result
result = tk.StringVar()
result_label = tk.Label(window, textvariable=result)
result_label.grid(row=11, column=1)

# Run the application
window.mainloop()
