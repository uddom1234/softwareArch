import tkinter as tk
from customer import Customer
from account import Account
from placingOrderProcess import placingOrder
def sessionAccount():
    global customer
    name = nameInput.get()
    email = emailInput.get()
    address = addressInput.get()
    username = usernameInput.get()
    password = passwordInput.get()

    try:
        with open(f'accounts.txt', 'r') as file:
            lines = file.readlines()
            if lines:
                for line in lines:
                    account_info = line.strip().split(', ')
                    account_dict = {info.split(': ')[0]: info.split(': ')[1] for info in account_info}
                    userName = account_dict['Username']
                    userEmail = account_dict['Email']
                    userPassword = account_dict['Password']

                    if userName == username or userEmail == email:
                        result.set("Account already created. ")
                    else:
                        customer = Customer(name, email, address)
                        customer.signUp(username, password)
                        currentAccount = customer.account
                        result.set(f"Account created for {name}")
                        window.destroy()
                        break

            else:
                customer = Customer(name, email, address)
                customer.signUp(username, password)
                currentAccount = customer.account
                result.set(f"Account created for {name}")
                window.destroy()


    except FileNotFoundError:
        customer = Customer(name, email, address)
        customer.signUp(username, password)
        currentAccount = customer.account
        result.set(f"Account created for {name}")
        window.destroy()

    if (customer):
        placingOrder(customer)

def login():
    username = loginUsernameInput.get()
    password = loginPasswordInput.get()
    try:
        with open(f'accounts.txt', 'r') as file:
            for line in file:
                account_info = line.strip().split(', ')
                account_dict = {info.split(': ')[0]: info.split(': ')[1] for info in account_info}
                userName = account_dict['Username']
                userPassword = account_dict['Password']

                if userName == username and userPassword == password:
                    customer = Customer(account_dict['Name'], account_dict['Email'], account_dict['Address'])
                    customer.account = Account(customer, username, password)
                    result.set(f"Signed in, Welcome {customer.name}!")
                    currentAccount = customer.account
                    window.destroy()

                elif userName == username and userPassword != password:
                    result.set("Incorrect password")

                else:
                    result.set(f"Account not found. Please create an account.")

    except FileNotFoundError:
        result.set(f"Account not found. Please create an account.")

    if(customer):
        placingOrder(customer)


# Create the main window
window = tk.Tk()
window.title("Online Healthy Food Store")

# Create labels, entries, and buttons for creating an account
nameHeader = tk.Label(window, text="Name:")
nameHeader.grid(row=0, column=0)
nameInput = tk.Entry(window)
nameInput.grid(row=1, column=0)

emailHeader = tk.Label(window, text="Email:")
emailHeader.grid(row=0, column=1)
emailInput = tk.Entry(window)
emailInput.grid(row=1, column=1)

addressHeader = tk.Label(window, text="Address:")
addressHeader.grid(row=0, column=2)
addressInput = tk.Entry(window)
addressInput.grid(row=1, column=2)

usernameHeader = tk.Label(window, text="Username:")
usernameHeader.grid(row=2, column=0)
usernameInput = tk.Entry(window)
usernameInput.grid(row=3, column=0)

passwordHeader = tk.Label(window, text="Password:")
passwordHeader.grid(row=2, column=1)
passwordInput = tk.Entry(window, show='*')
passwordInput.grid(row=3, column=1)

createButton = tk.Button(window, text="Create Account", command=sessionAccount)
createButton.grid(row=3, column=2)

breakHeader = tk.Label(window, text='---Login if you have an account---')
breakHeader.grid(row=4, column=1)

usernameHeader = tk.Label(window, text="Username:")
usernameHeader.grid(row=5, column=0)
loginUsernameInput = tk.Entry(window)
loginUsernameInput.grid(row=6, column=0)

passwordHeader = tk.Label(window, text="Password:")
passwordHeader.grid(row=5, column=1)
loginPasswordInput = tk.Entry(window, show='*')
loginPasswordInput.grid(row=6, column=1)

createButton = tk.Button(window, text="Login", command=login)
createButton.grid(row=6, column=2)

# Create a label for displaying the result
result = tk.StringVar()
resultHeader = tk.Label(window, textvariable=result)
resultHeader.grid(row=11, column=1)

# Run the application
window.mainloop()
