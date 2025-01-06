"""
Script based on the projekts found in https://github.com/karan/Projects 
This script finds all prime factors for a number 
"""

print("This script finds all prime factors for a number")

while True:
    try:
        number = int(input("Enter the number you whis to know the prime factors of:"))
        if number < 1:
            print ("The definition use for prime numbers are posetive numbers larger than 1, please try agine")
            continue
        break
    except ValueError:
        print("Please enter a number")

def is_prime(n):
   """test if the number it self is a prime number"""
   for i in range(2,n):
      if (n % i) == 0:
         return False
      else:
         return True

def prime_factors(n):
    """Find all prime factors of a given number."""
    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    return factors

factors = []

if is_prime(number) == True:
    print(f"{number}, is a prime number")
else:
    factors = prime_factors(number) # I only calculate the factors if it is not a prime number to uptimise time

if len(factors)==0:
    print("There are no prime factors") 
else:
    factors_string = " * ".join(map(str, factors))
    print(f"The primefactors of {number} are {factors_string}")