"""
A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,

a**2 + b**2 = c**2
For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

def is_pythagorean_triplet(a, b, c):
    return a**2 + b**2 == c**2

def find_pythagorean_triplet_with_sum(n):
    for a in range(3, (n - 3) / 3):
        for b in range(a + 1, (n - 1 - a) / 2):
            c = n - a - b
            if is_pythagorean_triplet(a, b, c):
                return [a, b, c]

triplet = find_pythagorean_triplet_with_sum(1000)

print triplet[0] * triplet[1] * triplet[2]  # prints 31875000
