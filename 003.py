import math
fac = []


def prime_factors(n):
    # Print the number of two's that divide n
    while n % 2 == 0:
        print("2", end=", ")
        fac.append(2)
        n = n / 2

    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    for i in range(3, int(math.sqrt(n)) + 1, 2):

        # while i divides n , print i and divide n
        while n % i == 0:
            print(i, end=", ")
            fac.append(i)
            n = n / i

    # Condition if n is a prime
    # number greater than 2
    if n > 2:
        fac.append(n)
        print(n)


prime_factors(600851475143)
print(fac)
