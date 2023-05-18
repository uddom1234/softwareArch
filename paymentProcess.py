import tkinter as tk

def paymentProcess(customer, order):
    def selectMethod(method):
        res = customer.account.requestPaymentMethod(method, order)
        result.set(res)


    window = tk.Tk()
    window.title("Online Healthy Food Store")

    nameHeader = tk.Label(window, text="Select Payment Method:")
    nameHeader.grid(row=0, column=1)
    paymentMethods = customer.payment_methods

    creditCardOpt = tk.Button(window, text=f'{paymentMethods[0]}', command=lambda:selectMethod(paymentMethods[0]))
    creditCardOpt.grid(row=1, column= 1)

    payPalOpt = tk.Button(window, text=f'{paymentMethods[1]}', command=lambda:selectMethod(paymentMethods[1]))
    payPalOpt.grid(row=2, column= 1)

    result = tk.StringVar()
    resultHeader = tk.Label(window, textvariable=result)
    resultHeader.grid(row=3, column=1)


    window.mainloop()
