from Tools.monteCarlo import (
    monteCarlo01,
    monteCarlo0INF,
    monteCarloAB,
    monteCarlo01_2,
    monteCarlo0INF_2
)
import math

N_SIM = 1_000_000


# Single-variable
# a)
def a(x):
    return (1 - (x ** 2)) ** (3/2)


# Expected: 0.58905
print(f'a) {monteCarlo01(a, N_SIM)}')


# b)
def b(x):
    return x / ((x ** 2) - 1)


# Expected: 0.49041
print(f'b) {monteCarloAB(b, 2, 3, N_SIM)}')


# c)
def c(x):
    return x / ((1 + x ** 2) ** 2)


# Expected: 0.5
print(f'c) {monteCarlo0INF(c, N_SIM)}')


# d)
def d(x):
    return 2 * math.e ** (- x ** 2)


# Expected: 1.77245
print(f'd) {monteCarlo0INF(d, N_SIM)}')


# Multiple-variable
# e)
def e(x, y):
    return math.e ** ((x + y) ** 2)


# Expected: 4.88916
print(f'e) {monteCarlo01_2(e, N_SIM)}')


# f)
def I_f(x, y):
    if y < x:
        return 1
    else:
        return 0


def f(x, y):
    return math.e ** (- x - y) * I_f(x, y)


# Expected: 0.5
print(f'f) {monteCarlo0INF_2(f, N_SIM)}')
