"""
Script based on the projects found in https://github.com/karan/Projects 
This script finds the next prime number 
The description of the task was:
Have the program find prime numbers until the user stops asking for the next one.
"""
def is_prime(n):
    """ Test if the number n is a prime number """
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):  
        if n % i == 0:
            return False
    return True

print("2 is the first prime number, do you want the next? y/n:")

current_prime = 2 

while True:
    user_input = input()
    if user_input == "y":
        temp_nump = current_prime + 1
        while not is_prime(temp_nump): 
            temp_nump += 1
        current_prime = temp_nump
        print(f"The next prime number is {current_prime}. Do you want the next? y/n:")
    elif user_input == "n":
        print("Bye bye")
        break
    else:
        print("Invalid input. Please type 'y' for yes or 'n' for no.")




