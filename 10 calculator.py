"""
Script based on the projects found in https://github.com/karan/Projects 
Calculator - 
A simple calculator to do basic operators. Make it a scientific calculator for added complexity.
""" 
import tkinter as tk
from tkinter import messagebox, ttk 
import math


def main():
    """ Lunches the calculator """
    root = tk.Tk()
    root.title('Calculator')
    root.geometry("200x300")

    def add_to_end(text):
        """Adds text to the end of string in calculator window"""
        current_text = calculator_window.get()
        calculator_window.delete(0, tk.END)
        calculator_window.insert(0, current_text + text)

    def add_to_start(text):
        """Adds text to the start of string in calculator window"""
        current_text = calculator_window.get()
        calculator_window.delete(0, tk.END)
        calculator_window.insert(0, text + current_text )

    def remove_from():
        """removes text to the end of string in calculator window"""
        current_text = calculator_window.get()
        calculator_window.delete(0, tk.END)
        calculator_window.insert(0, current_text[:len(current_text)-1])

    pi = math.pi

    def calculate():
        try:
            expression = calculator_window.get()
            # Evaluate the expression using eval(), with support for math functions
            result = eval(expression, {"__builtins__": None}, math.__dict__)
            calculator_window.delete(0, tk.END)
            calculator_window.insert(0, str(result))
        except Exception as e:
            calculator_window.delete(0, tk.END)
            calculator_window.insert(0, "Error")




#----- Below is the GUI with buttons and places to enter inputs
    calculator_window = tk.Entry(root)
    calculator_window.grid(row=0, column=0, columnspan=4)

#--- 1st row of buttons 
    button_procent = tk.Button(root, text = "\u03c0", height=2, width=3, command = lambda: add_to_end("pi"))
    button_procent.grid(row=1, column=0)

    button_parenthesis_start = tk.Button(root, text = "(", height=2, width=3, command = lambda: add_to_end("("))
    button_parenthesis_start.grid(row=1, column=1)

    button_parenthesis_end = tk.Button(root, text = ")", height=2, width=3, command = lambda: add_to_end(")") )
    button_parenthesis_end.grid(row=1, column=2)

    button_backspace = tk.Button(root, text = "\u232b", height=2, width=3, command = lambda: remove_from())
    button_backspace.grid(row=1, column=3)

#--- 2th row of buttons 
    button_one_over_x = tk.Button(root, text = "1/x", height=2, width=3, command = lambda: add_to_start("1/(") )
    button_one_over_x.grid(row=2, column=0)

    button_to_the_power_of_two = tk.Button(root, text = "^2", height=2, width=3, command = lambda: add_to_end("^2"))
    button_to_the_power_of_two.grid(row=2, column=1)

    button_sqr_root = tk.Button(root, text = "sqrt", height=2, width=3, command = lambda: add_to_end("sqrt(") )
    button_sqr_root.grid(row=2, column=2)

    button_division = tk.Button(root, text = "/", height=2, width=3, command = lambda: add_to_end("/"))
    button_division.grid(row=2, column=3)

#--- 3th row of buttons 
    button_seven = tk.Button(root, text = "7", height=2, width=3, command = lambda: add_to_end("7"))
    button_seven.grid(row=3, column=0)

    button_eight = tk.Button(root, text = "8", height=2, width=3, command = lambda: add_to_end("8"))
    button_eight.grid(row=3, column=1)

    button_nine = tk.Button(root, text = "9", height=2, width=3, command = lambda: add_to_end("9"))
    button_nine.grid(row=3, column=2)

    button_multiply = tk.Button(root, text = "*", height=2, width=3, command = lambda: add_to_end("*"))
    button_multiply.grid(row=3, column=3)

#--- 4th row of buttons 
    button_four = tk.Button(root, text = "4", height=2, width=3, command = lambda: add_to_end("4"))
    button_four.grid(row=4, column=0)

    button_five = tk.Button(root, text = "5", height=2, width=3, command = lambda: add_to_end("5"))
    button_five.grid(row=4, column=1)

    button_six = tk.Button(root, text = "6", height=2, width=3, command = lambda: add_to_end("6"))
    button_six.grid(row=4, column=2)

    button_subtract = tk.Button(root, text = "-", height=2, width=3, command = lambda: add_to_end("-"))
    button_subtract.grid(row=4, column=3)

#--- 5th row of buttons 
    button_one = tk.Button(root, text = "1", height=2, width=3, command = lambda: add_to_end("1"))
    button_one.grid(row=5, column=0)

    button_two = tk.Button(root, text = "2", height=2, width=3, command = lambda: add_to_end("2"))
    button_two.grid(row=5, column=1)

    button_three = tk.Button(root, text = "3", height=2, width=3, command = lambda: add_to_end("3"))
    button_three.grid(row=5, column=2)

    button_addition = tk.Button(root, text = "+", height=2, width=3, command = lambda: add_to_end("+"))
    button_addition.grid(row=5, column=3)

#--- 6th row of buttons 
    button_plus_minus = tk.Button(root, text = "AC", height=2, width=3, command = lambda: calculator_window.delete(0, tk.END))
    button_plus_minus.grid(row=6, column=0)

    button_zero = tk.Button(root, text = "0", height=2, width=3, command = lambda: add_to_end("0"))
    button_zero.grid(row=6, column=1)

    button_decimal_point = tk.Button(root, text = ".", height=2, width=3, command = lambda: add_to_end("."))
    button_decimal_point.grid(row=6, column=2)

    button_enter = tk.Button(root, text = "=", height=2, width=3, command = lambda: calculate())
    button_enter.grid(row=6, column=3)

    root.mainloop()


main()
