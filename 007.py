'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
'''
import math

my_primes = [2, 3, 5]


def gen_primes(cnt):
    for i in range(7,9999999999999,2):
        if not(any(i%j == 0 for j in range(3,int(math.sqrt(i))+1))):
            my_primes.append(i)
        if len(my_primes) >= cnt:
            return


if __name__ == "__main__":
    gen_primes(10001)
    print("Nth Prime: ", my_primes[-1])
    print(my_primes)