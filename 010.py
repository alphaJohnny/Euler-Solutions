import math


def gen_primes(till):
    my_primes = [2, 3, 5]
    for i in range(7, till, 2):
        if not (any(i % j == 0 for j in range(3, int(math.sqrt(i)) + 1))):
            my_primes.append(i)
    return my_primes


if __name__ == "__main__":
    my_primes = gen_primes(2000000)
    print(my_primes)
    print(sum(my_primes))
