

# make a list of triangle numbers
import math


def number_of_divisors(num):

    divisors = 0
    sqrt = int(math.sqrt(n))
    for i in range(1, sqrt):
        if(n % i == 0 ):
            # Need More Input
            divisors += 2
    if(sqrt * sqrt == num):
        divisors -= 1
    return divisors

if __name__ == '__main__':
    n = 0
    i = 1
    while(number_of_divisors(n) < 500):
        n += i
        # why are we pushing up higher and higher steps
        i += 1

    print("Number :", n)
    print("Num of Divisors: ",number_of_divisors(n))