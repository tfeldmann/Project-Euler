# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

LIMIT = 2000000

def isprime(n):
    """check if integer n is a prime"""
    # range starts with 2 and only needs to go up the squareroot of n
    for x in range(2, int(n**0.5)+1):
        if n % x == 0:
            return False
    return True


result = 2
for x in range(3, LIMIT, 2):
    if isprime(x):
        result += x

print result  # prints 142913828922
