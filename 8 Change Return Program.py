"""
Script based on the projects found in https://github.com/karan/Projects 
Change Return Program - 
The user enters a cost and then the amount of money given. 
The program will figure out the change and the number of quarters, dimes, nickels, and pennies needed for the change.
"""
import tkinter as tk
from tkinter import messagebox, ttk 

def change_return_calculator():
    root = tk.Tk()
    root.title('Change return calculator')
    root.geometry("600x400")

    def display_result(text):
        """Clear existing result and display new text."""
        for widget in root.grid_slaves():
            if int(widget.grid_info()["row"]) == 7:
                widget.destroy()
        label = tk.Label(root, text=text)
        label.grid(row=7, column=1)

    def is_float(value, query):
        """ 
        Checks that inputted values are floats larger than 0
        """
        error_occurred = False 
        if not value:
            messagebox.showerror("Error", f"Please enter a value for {query}.")
            error_occurred = True 
        try:
            value = float(value)
            if value < 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", f"{query} must be a posetive number larger than 0.")
            error_occurred = True        
        if error_occurred:
            return None
        return float(value)

    def calculate_change():
        """
        calculates the return change 
        calculates in cents so I can do calculations in ints as I had problems using floats resulting in missing 1 cent 
        """
        list_of_currency = [10000, 5000, 2000, 1000, 500, 200, 100, 50, 25, 10, 5, 1]  
        price = is_float(entry_price.get(), "Price")
        paid = is_float(entry_paied.get(), "Paied")
        
        if paid < price:
            display_result("The customer has not paid enough")
            return (None)
        
        price = int(round(price * 100))
        paid = int(round(paid * 100))       
        change = paid - price
        change_distribution = {}

        for currency in list_of_currency:
            count = change // currency
            if count > 0:
                change_distribution[currency] = count
                change -= count * currency
        
        if not change_distribution:
            display_result("No change is needed.")
        else:
            result_text = "Change to return:\n"
            result_text += "\n".join([f"{count} x {currency / 100}" for currency, count in change_distribution.items()])
            display_result(result_text)   

    #----- Below is the GUI with buttons and places to enter inputs
    lable_price = tk.Label(root, text = 'Price')
    lable_price.grid(row=1,column=0)
    entry_price = tk.Entry(root)
    entry_price.grid(row=1,column=1)

    lable_paied = tk.Label(root, text = 'Paied')
    lable_paied.grid(row=2,column=0)
    entry_paied = tk.Entry(root)
    entry_paied.grid(row=2,column=1)

    button_calculate = tk.Button(root, text = "Calculate return change", command = calculate_change)
    button_calculate.grid(row=3,column=1)

    root.mainloop()

change_return_calculator()

