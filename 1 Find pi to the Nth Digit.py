"""
Script based on the projects found in https://github.com/karan/Projects 
This script finds the nth number of pi
"""
import math

print("This script finds", chr(0x000003C0), "to the n\'th position after the decimal point")

while True:
    try:
        pi_number = int(input("Enter the number of digits of " + chr(0x000003C0) + " you wish to know: "))
        if pi_number < 0:
            print ("The number can\'t be negative try again")
            continue
        break
    except ValueError:
        print("Your input needs to be a positive whole number, please try again.")
        
pi_str = f"{math.pi:.{pi_number}f}"
print(f"{chr(0x000003C0)} to the {pi_number} decimal places is: {pi_str}")
