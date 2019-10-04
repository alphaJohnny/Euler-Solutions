"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

# solution = take multiple of primes except for primes that are already accommodated in higher numbers


check_list = [11, 13, 14, 15, 16, 17, 18, 19, 20]


# a valid number will be a multiple of 20
def find_solution():
    # for i in range(20*19*18*17, 99999999999, 20):
    for i in range(2520, 99999999999, 2520):
        if all(i % n == 0 for n in check_list):
            return i
    return None


if __name__ == '__main__':
    sol = find_solution()
    if sol is None:
        print('nothing till the 11 9\'s')
    else:
        print("Answer is : ", sol)
