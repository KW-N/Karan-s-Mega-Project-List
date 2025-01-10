"""
Script based on the projects found in https://github.com/karan/Projects 
Mortgage Calculator - 
Calculate the monthly payments of a fixed term mortgage over given Nth terms at a given interest rate. 
Also, figure out how long it will take the user to pay back the loan. 
For added complexity, add an option for users to select the compounding interval (Monthly, Weekly, Daily, Continually).
I have decided to do this with a GUI using Tkinter for the challenge.
"""
import tkinter as tk
from tkinter import messagebox, ttk 


def check_value_input(value, query):
    """ Checks that values are inputted correctly and are different from 0 """
    error_occurred = False 
    if not value:
        messagebox.showerror("Error", f"Please enter a value for {query}.")
        error_occurred = True 
    try:
        value = float(value)
        if value == 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", f"{query} must be a valid non-zero number.")
        error_occurred = True
    if error_occurred:
        return None
    return float(value)

def mortgage_calculator():
    root = tk.Tk()
    root.title('Mortgage calculator')
    root.geometry("600x400")

    def check_inputs(mortgage, intrest_rate, monthly_paymentn):
        """ Validates that the inputs are in the right format """
        mortgage_valid = check_value_input(mortgage, "Mortgage amount")
        intrest_rate_valid = check_value_input(intrest_rate, "Intrest rate")
        monthly_paymentn_valid = check_value_input(monthly_paymentn, "Monthly payment")
        if not all([mortgage_valid, intrest_rate_valid, monthly_paymentn_valid]):
            return  
        main(mortgage_valid, intrest_rate_valid, monthly_paymentn_valid)

    def calculate_mortgage():
        """ The function that runs when the calculate_mortgage button is pressed """
        check_inputs(entry_mortgage.get(),
                     entry_intrest_rate.get(),
                     entry_monthly_payment.get())

    def display_result(text):
        "" "Clear existing results and display new text """
        for widget in root.grid_slaves():
            if int(widget.grid_info()["row"]) == 7:
                widget.destroy()
        label = tk.Label(root, text=text)
        label.grid(row=7, column=1)

    def main(mortgage_valid, intrest_rate_valid, monthly_paymentn_valid):
        compounding_interval = drop_down_compounding_interval.get()
        if compounding_interval == "Daily":
            compounding_interval = 30.5         # Avrage days in a month
        elif compounding_interval == "Weekly":
            compounding_interval = 4.34         # Avrage weeks in a month
        elif compounding_interval == "Monthly":
            compounding_interval = 1            # Avrage months in a month
        elif compounding_interval == "Yearly":
            compounding_interval = 1/12         # Avrage year in a month 

        if ( (mortgage_valid + mortgage_valid * (intrest_rate_valid * compounding_interval / 100 ) - monthly_paymentn_valid) ) > mortgage_valid:
            display_result("This  mortgage will never be payed of")

        else:
            months = 0
            while mortgage_valid > 0:
                mortgage_valid += mortgage_valid * (intrest_rate_valid * compounding_interval / 100)    # Adds monthly intrest rate
                mortgage_valid -= monthly_paymentn_valid                                                # Subtract the monthly payment
                months += 1                                                                             # Increment month counter
                if mortgage_valid < 0:
                    mortgage_valid = 0 
            
            display_result(f"The mortgage will take {months} months to be payed fully of")


    #----- Below is the GUI with buttons and places to enter inputs
    lable_mortgage = tk.Label(root, text = 'Mortgage amount')
    lable_mortgage.grid(row=1,column=0)
    entry_mortgage = tk.Entry(root)
    entry_mortgage.grid(row=1,column=1)

    lable_intrest_rate = tk.Label(root, text = 'Intrest rate')
    lable_intrest_rate.grid(row=2,column=0)
    entry_intrest_rate = tk.Entry(root)
    entry_intrest_rate.grid(row=2,column=1)    

    lable_monthly_payment = tk.Label(root, text = 'Monthly payment')
    lable_monthly_payment.grid(row=3,column=0)
    entry_monthly_payment = tk.Entry(root)
    entry_monthly_payment.grid(row=3,column=1)  

    drop_down_compounding_interval= tk.Label(root, text = 'Compounding interval')
    drop_down_compounding_interval.grid(row=4,column=0)
    drop_down_compounding_interval = ttk.Combobox(state="readonly",
                                                  values=["Daily", "Weekly", "Monthly", "Yearly" ])
    drop_down_compounding_interval.grid(row=4,column=1)
    drop_down_compounding_interval.set("Yearly") 

    button_calculate = tk.Button(root, text = "Calculate time to pay mortgage", command = calculate_mortgage)
    button_calculate.grid(row=6,column=1)

    root.mainloop()

mortgage_calculator()
