"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers
"""


def reverse(s):
    return s[::-1]


def is_palindrome(s):
    rev = reverse(s)
    if s == rev:
        return True
    return False


def range_2d(r1st, r1end, r1inc, r2st, r2end, r2inc):
    for r in range(r1st, r1end, r1inc):
        for c in range(r2st, r2end, r2inc):
            yield r, c


for i, j in range_2d(999, 900, -1, 999, 900, -1):
    print("I = ", i, " J = ", j, " Num = ", i*j)
    if is_palindrome(str(i*j)):
        print(i*j)
        break


