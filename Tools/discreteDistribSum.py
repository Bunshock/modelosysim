"""
Calculator for probabilities P(a <= X <= b) for a given discrete v.a.
If a = b, then it calculates P(X = a)
"""

import math
import matplotlib.pyplot as plt
import numpy as np

# Discrete distribution data
DISC_DIST_ARGS = [
    [
        'Binomial',
        ['p', 'n'],
        lambda p, n, x: math.comb(n, x) * (p ** x) * ((1-p) ** (n-x))
    ],
    [
        'Poisson',
        ['lambda'],
        lambda lamb, x: math.e**(-lamb) * ((lamb**x) / math.factorial(x))
    ],
    [
        'Geometric',
        ['p'],
        lambda p, x: p * ((1-p) ** (x-1))
    ],
    [
        'BinomialNeg',
        ['r', 'p'],
        lambda p, r, x: math.comb(x-1, r-1) * (p ** r) * ((1-p) ** x-r)
    ],
    [
        'Hipergeometric',
        ['n', 'N', 'M'],
        lambda n, N, M, x: (math.comb(N, x)*math.comb(M, n-x)) / math.comb(N+M, x)
    ],
    [
        'Uniform',
        ['n'],
        lambda n, x: 1 / n
    ]
]


# X ~ B(n, p)
def checkBinomial(p, n, a, b):
    assert 0 <= p <= 1, 'p is an invalid probability value'
    assert n > 0, 'n should be a positive integer'
    assert 0 <= a <= n, 'required: 0 <= a <= n'
    assert 0 <= b <= n, 'required: 0 <= b <= n'
    assert b >= a, 'required: b >= a'


# X ~ P(lamb)
def checkPoisson(lamb, a, b):
    assert lamb > 0
    assert a >= 0
    assert b >= a


# X ~ Geom(p)
def checkGeometric(p, a, b):
    assert 0 <= p <= 1
    assert a >= 1
    assert b >= a


# X ~ Bn(r, p)
def checkBinomialNeg(p, r, a, b):
    assert 0 <= p <= 1
    assert r >= 1
    assert a >= r
    assert b >= a


# X ~ H(n, N, M)
def checkHipergeometric(n, N, M, a, b):
    assert b <= n
    assert n - a <= M
    assert 1 <= n <= N + M
    

# X ~ U{1, n}
def checkUniform(n, a, b):
    assert n >= 1
    assert a >= 1
    assert b >= a
    assert b <= n


# Function that calculates P(a <= X <= b)
def distribSum(distrib_index, a, b, *params):
    # Check preconditions
    globals()[f'check{DISC_DIST_ARGS[distrib_index][0]}'](*params, a, b)

    # Get distribution function
    distrib_fun = DISC_DIST_ARGS[distrib_index][2]

    # Sum P(X=a) + ... + P(X=b)
    sum = 0
    x_vec, y_vec = [], []
    for x in range(a, b+1):
        y = distrib_fun(*params, x)
        sum += y

        x_vec.append(x)
        y_vec.append(y)

    return sum, x_vec, y_vec


if __name__ == '__main__':
    # Auxiliar function to interpret input parameters
    def interpretedNumberType(x):
        if '.' in x:
            return float(x)
        else:
            return int(x)

    # Print available distributions
    print('Available distributions')
    for i in range(len(DISC_DIST_ARGS)):
        print(f'{i+1} - {DISC_DIST_ARGS[i][0]}(', end='')
        for j in range(len(DISC_DIST_ARGS[i][1])):
            if j == len(DISC_DIST_ARGS[i][1]) - 1:
                print(DISC_DIST_ARGS[i][1][j], end='')
            else:
                print(DISC_DIST_ARGS[i][1][j], end=',')
        print(')')

    # Select desired distribution
    distr = int(input('Enter desired distribution number: ')) - 1
    assert distr in range(len(DISC_DIST_ARGS))

    # Input every distribution parameter
    args = []
    for i in range(len(DISC_DIST_ARGS[distr][1])):
        arg = input(f'Input {DISC_DIST_ARGS[distr][1][i]} value: ')
        args.append(interpretedNumberType(arg))

    a = interpretedNumberType(input('Enter lower bound (a): '))
    b = interpretedNumberType(input('Enter upper bound (b): '))

    # Print result
    result, x_vec, y_vec = distribSum(distr, a, b, *args)
    print(f'P({a} <= X <= {b}) = {result}')
    
    # Show every calculated point in a graph
    plt.scatter(x_vec, y_vec)

    # Set x and y axis
    plt.xticks(range(math.floor(min(x_vec)), math.ceil(max(x_vec))+1))

    y_step = max(y_vec) / 15
    plt.yticks(np.arange(min(y_vec), max(y_vec)+y_step, y_step))
    
    # Draw lines between x axis and graph points
    plt.vlines(x_vec, 0, y_vec)
    
    # Show horizontal grid lines
    plt.grid(axis='y')

    # Show the graph
    plt.show()