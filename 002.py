
def fib_to(n):
    x = 0
    y = 1
    z = 0
    ret = 0
    while z < n:
        print("x = ", x, " y = ", y, " z = ", z)

        if z % 2 == 0:
            ret += z

        # increment
        z = x + y
        x, y = y, z

    return ret


print(fib_to(4000000))
