# A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,
#
# a**2 + b**2 = c**2
# For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

def is_pythagorean_triplet(a, b, c):
    return a**2 + b**2 == c**2

def find_pythagorean_triplet_with_sum(n):
    RANGE = range(1, n)
    for h in RANGE:
        for j in RANGE:
            for k in RANGE:
                if h + j + k == n and is_pythagorean_triplet(h, j, k):
                    return [h, j, k]

triplet = find_pythagorean_triplet_with_sum(1000)

print triplet[0] * triplet[1] * triplet[2]  # prints 31875000
