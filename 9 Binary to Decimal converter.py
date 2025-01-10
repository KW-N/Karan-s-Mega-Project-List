"""
Script based on the projects found in https://github.com/karan/Projects 
Binary to Decimal and Back Converter - 
Develop a converter to convert a decimal number to binary or a binary number to its decimal equivalent.
""" 
import tkinter as tk
from tkinter import messagebox, ttk 

def main():
    """ The main body of the function """
    root = tk.Tk()
    root.title('Change return calculator')
    root.geometry("300x150")

    def display_result(text, position):
        """ Clear existing result and display new text in the tkinter GUI """
        for widget in root.grid_slaves():
            if int(widget.grid_info()["row"]) == position:
                widget.destroy()
        label = tk.Label(root, text=text)
        label.grid(row=position, column=1)
    
    def convert_binary():
        """ 
        First, this function validates the input in the binary box
        Next, the function converts the binary number to a decimal number
        Finally, it prints the number in the GUI using display_results  
        """
        binary = entry_binary.get()

        if not binary: #Error if no input is given
            messagebox.showerror("Error", f"Please enter a binary value to convert to a decimal value.")
            return
        
        if not all(char in "01" for char in binary):  # Check if input only contains 0 and 1
            messagebox.showerror("Error", "Invalid input. A binary number must contain only 0 and 1.")
            return
        
        try: # Convert binary to decimal
            decimal_result = int(binary, 2)
            display_result(f"{binary} in decimal is {decimal_result}", 6)
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {e}")

    def convert_decimal():
        """ 
        First, this function validates the input decimal value box
        Next, the function converts the decimal number to a binary number
        Finally, it prints the number in the GUI using display_results 
        
        The numbers after the decimal point are handled as binary fractions:
        0.1   = 1/2 = 0.5
        0.01  = 1/4 = 0.25
        0.001 = 1/8 = 0.125
        """
        decimal = entry_decimal.get()

        if not decimal: #Error if no input is given
            messagebox.showerror("Error", f"Please enter a decimal value to convert to a binary value.")
            return

        try: #Error if the input is not a number 
            value = float(decimal)
        except ValueError:
            messagebox.showerror("Error", f"The decimal number must be a number.")
            return
        
        try:    
            value = float(decimal)
            integer_part = int(value)
            binary_integer = bin(integer_part).replace("0b", "")
            fractional_part = value - integer_part
            binary_fraction = []

            while fractional_part > 0 and len(binary_fraction) < 10:  # Limit to 10 binary places
                fractional_part *= 2
                bit = int(fractional_part)
                binary_fraction.append(str(bit))
                fractional_part -= bit
            if binary_fraction:
                binary_result = f"{binary_integer}.{''.join(binary_fraction)}"
            else:
                binary_result = binary_integer
            display_result(f"{decimal} in binary is {binary_result}", 10)

        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {e}")

#----- Below is the GUI with buttons and places to enter inputs
    lable_binary = tk.Label(root, text = 'Binary number')
    lable_binary.grid(row=4,column=0)
    entry_binary = tk.Entry(root)
    entry_binary.grid(row=4,column=1)

    button_convert_binary = tk.Button(root, text = "Convert to a decimal number", command = convert_binary)
    button_convert_binary.grid(row=5,column=1)

    lable_decimal = tk.Label(root, text = 'Decimal number')
    lable_decimal.grid(row=8,column=0)
    entry_decimal = tk.Entry(root)
    entry_decimal.grid(row=8,column=1)

    button_convert_decimal = tk.Button(root, text = "Convert to a binary number", command = convert_decimal)
    button_convert_decimal.grid(row=9,column=1)

    root.mainloop()

main()
