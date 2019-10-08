"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

def triplet():
    for i in range(1, 500):
        for j in range(1, 500):
            k = 1000 - (i + j)
            #print("I : ", i,"J : ", j,"K :", k)
            if k ** 2 == i ** 2 + j ** 2:
                return [i, j, k]


if __name__ == "__main__":
    i, j, k = triplet()
    print(i, j, k)
    print("Product : ", i*j*k)