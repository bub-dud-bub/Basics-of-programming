import math


def func_f(x):
    return math.cos(1.7**(x+1) - 2.7)


def func_g(x):
    return 2**x + x**2 - 2


def func_a_ij(i, m):
    sum = float(0)
    for j in range(1, m+1):
        sum += (func_f(i) + func_g(j))
    return math.fabs(sum)


def func_n_a(m, n):
    m = min(m, n)
    max_value = float()

    for i in range(1, m+1):
        max_value = max(max_value, func_a_ij(i, m))

    return max_value

print(func_n_a(1000, 1000))
#0.928s
