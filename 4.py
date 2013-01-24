# A palindromic number reads the same both ways. The largest palindrome made
# from the product of two 2-digit numbers is 9009 = 91 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def ispalindrome(n):
    s = str(n)
    r = s[::-1]
    return s == r

def biggestpalindrome():
    x = 999
    while x > 100:
        y = 999
        while y > 100:
            n = x * y
            if ispalindrome(n):
                return {"product": n, "n1": x, "n2": y}
            y = y - 1
        x = x - 1

print biggestpalindrome()
