# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
# that the 6th prime is 13.
#
# What is the 10 001st prime number?

def isprime(n):
    """check if integer n is a prime"""
    # range starts with 2 and only needs to go up the squareroot of n
    for x in range(2, int(n**0.5)+1):
        if n % x == 0:
            return False
    return True

n = 1
c = 0
while not c == 10001:
    n += 1
    if isprime(n):
        c += 1
print n  # prints 104743
