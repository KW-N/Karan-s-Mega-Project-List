"""
Script based on the projects found in https://github.com/karan/Projects 
This script finds the nth number of e
"""
import math

print("This script finds e to the n\'th position after the decimal point")

while True:
    try:
        e_number = int(input("Enter the number of digits of e you wish to know: "))
        if e_number < 0:
            print ("The number can\'t be negative try again")
            continue
        break
    except ValueError:
        print("Your input needs to be a positive whole number, please try again.")
        
e_str = f"{math.e:.{e_number}f}"
print(f"e to the {e_number} decimal places is: {e_str}")
