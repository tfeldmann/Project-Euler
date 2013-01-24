# 2520 is the smallest number that can be divided by each of the numbers from
# 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the
# numbers from 1 to 20?

def divisible(n):
    for d in range(20, 3, -1):
        if not n % d == 0:
            return False
    return True

n = 20
while not divisible(n):
    n = n + 20

print n  # 232792560
