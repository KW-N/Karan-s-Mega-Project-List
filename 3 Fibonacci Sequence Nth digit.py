"""
Script based on the projekts found in https://github.com/karan/Projects 
This script generates the n'th number in the fibonarcci sequence
"""
print("This script generates the n\'th number in the fibonarcci sequence")

while True:
    try:
        nth_fib = int(input("Enter the number you want from the fibonacci sequence: "))
        if nth_fib < 0:
            print ("The number can\'t be negative try again")
            continue
        break
    except ValueError:
        print("Your input needs to be a positive whole number, please ttry again.")

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

fib_number = fibonacci(nth_fib)
print(f"The {nth_fib} number in the Fibonacci sequence is: {fib_number}")