"""
General idea for Monte Carlo algorithm implementation on (0, 1):
"""

from random import random

# INTEGRALES DE UNA VARIABLE #


# Interval : (0, 1)
def monteCarlo01(g, N):
    integral = 0
    for _ in range(N):
        X = random()
        integral += g(X)
    return integral / N


# Interval : (a, b)    (a < b)
def monteCarloAB(g, a, b, N):
    integral = 0
    for _ in range(N):
        X = random()
        integral += g(a + (b-a) * X)
    return integral * (b-a) / N


"""
Another way to implement the method for (a, b) is to define
h(x) = g(a + (b-a) * x) * (b-a) , y in (0, 1)
and use monteCarlo01 method. Same goes for (0, inf)
and h(x) = (1/x^2) * g(1/x  - 1)
"""


# Interval : (0, inf)
def monteCarlo0INF(g, N):
    integral = 0
    for _ in range(N):
        X = random()
        integral += g((1/X) - 1) / (X ** 2)
    return integral / N

# INTEGRALES MULTIPLES #


# Interval : X->(0, 1), Y->(0, 1)
def monteCarlo01_2(g, N):
    integral = 0
    for _ in range(N):
        X, Y = random(), random()
        integral += g(X, Y)
    return integral / N


# Interval : X->(a, b), Y->(c, d)
def monteCarloAB_2(g, a, b, c, d, N):
    integral = 0
    for _ in range(N):
        X, Y = random(), random()
        integral += g(a + (b-a)*X, c + (d-c)*Y)
    return integral * (b-a) * (d-c) / N


# Interval : X->(0, inf), Y->(0, inf)
def monteCarlo0INF_2(g, N):
    integral = 0
    for _ in range(N):
        X, Y = random(), random()
        integral += g(1/X - 1, 1/Y - 1) / ((X ** 2) * (Y ** 2))
    return integral / N
