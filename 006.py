

def sum_of_squares(num):
    s = 0
    for i in range(1, num+1):
        s += i**2
    return s

if __name__ == '__main__':
    sq_of_sum = sum(range(1, 100+1))**2
    sum_of_sq = sum_of_squares(100)
    print("Sq of sum: ", sq_of_sum)
    print("Sum of sq: ", sum_of_sq)
    print("Diff : ", sq_of_sum - sum_of_sq)