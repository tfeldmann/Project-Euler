# A palindromic number reads the same both ways. The largest palindrome made
# from the product of two 2-digit numbers is 9009 = 91 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def ispalindrome(n):
    s = str(n)
    r = s[::-1]
    return s == r

def biggestpalindrome():
    possible_solutions = []
    x = 999
    while x > 99:
        y = 999
        while y > 99:
            n = x * y
            if ispalindrome(n):
                possible_solutions.append(n)
            y = y - 1
        x = x - 1

    return max(possible_solutions)

print biggestpalindrome()
