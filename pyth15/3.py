import numpy as np


def func_f(x):
    return np.cos(1.7**(x+1) - 2.7)


def func_g(x):
    return 2**x + x**2 - 2


def func_a_ij(i, m):
    x = np.linspace(1, m, 10)
    mesh = np.piecewise(
    x,
    [x],
    [np.fabs(func_f(i) + func_g(x))]
    )
    sum = float(np.sum(mesh))
    return sum


def func_n_a(m, n):
    m = min(m, n)
    x = np.linspace(1, m, 10)
    mesh = []
    for i in x:
        mesh.append(func_a_ij(i, m))
    max_value = float(np.max(mesh))
    return 2*max_value

print(func_n_a(1000, 1000))
#0.83
