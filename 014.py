import sys


def generate_collatz_seq(n):
    if(n == 1):
        return([n])
    if(n % 2 == 0):
        n2 = n / 2
    else:
        n2 = 3 * n + 1
    return [n] + generate_collatz_seq(int(n2))


if __name__ == '__main__':
    sys.setrecursionlimit(1000)
    max_elements = 0
    max_elements_num = 0
    for i in range(1,1000000):
        print("Current Number: ", i)
        col_list = generate_collatz_seq(i)
        if len(col_list) > max_elements:
            max_elements = len(col_list)
            max_elements_num = i
    print("Max number of elements: ", max_elements)
    print("The number that has max elements: ",max_elements_num)
