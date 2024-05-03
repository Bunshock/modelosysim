"""
Calculator for probabilities P(a <= X <= b) for a given discrete v.a.
"""

import math
from monte_carlo import monteCarlo01, monteCarloAB, monteCarlo0INF

CONT_DIST_ARGS = [
    [
        'Uniform',
        ['a', 'b'],
        lambda a, b, x: 1 / (b - a) * (a < x < b)
    ],
    [
        'Normal',
        ['mu', 'sig'],
        lambda mu, sig, x: (1/(sig*math.sqrt(2*math.pi))) * (math.e ** -(((x-mu)**2)/(2*(sig**2))))
    ],
    [
        'Exponential',
        ['lamb'],
        lambda lamb, x: lamb * (math.e ** (-lamb * x)) * (x > 0)
    ],
    [
        'Lognormal',
        ['mu', 'sig'],
        lambda mu, sig, x: (1/(x*math.sqrt(2*math.pi*(sig**2)))) * (math.e ** -(((math.log(x)-mu)**2)/(2*(sig**2)))) * (x > 0)
    ],
    [
        'Gamma',
        ['alpha', 'beta'],
        lambda alpha, beta, x: (1/math.gamma(alpha)) * (beta**(-alpha)) * (x**(alpha-1)) * (math.e**(-x/beta)) * (x > 0)
    ],
    [
        'Weibull',
        ['alpha', 'beta'],
        lambda alpha, beta, x: alpha * (beta**(-alpha)) * (x**(alpha-1)) * (math.e**((-x/beta)**alpha)) * (x > 0)
    ]
]


if __name__ == '__main__':
    # Auxiliar function to interpret input parameters
    def interpretedNumberType(x):
        if '.' in x:
            return float(x)
        elif x == 'inf':
            return x
        else:
            return int(x)

    # Print available distributions
    print('Available distributions')
    for i in range(len(CONT_DIST_ARGS)):
        print(f'{i+1} - {CONT_DIST_ARGS[i][0]}(', end='')
        for j in range(len(CONT_DIST_ARGS[i][1])):
            if j == len(CONT_DIST_ARGS[i][1]) - 1:
                print(CONT_DIST_ARGS[i][1][j], end='')
            else:
                print(CONT_DIST_ARGS[i][1][j], end=',')
        print(')')

    # Select desired distribution
    distr = int(input('Enter desired distribution number: ')) - 1
    assert distr in range(len(CONT_DIST_ARGS))

    # Input every distribution parameter
    args = []
    for i in range(len(CONT_DIST_ARGS[distr][1])):
        arg = input(f'Input {CONT_DIST_ARGS[distr][1][i]} value: ')
        args.append(interpretedNumberType(arg))

    a = interpretedNumberType(input('Enter lower bound (a): '))
    b = interpretedNumberType(input('Enter lower bound (b): '))
    assert b == 'inf' or b > a

    # Input number of simulations
    N_SIM = int(input('How many times will the value be simulated? '))
    assert N_SIM > 0

    for _ in range(N_SIM):
        N = int(input('How many iterations for next simulation? '))

        # See which of the three Monte Carlo methods to use and adapt
        # to them
        distr_fun = CONT_DIST_ARGS[distr][2]
        result = 0
        if b == 'inf':
            if a == 0:
                result = monteCarlo0INF(lambda x: distr_fun(*args, x), N)
            elif a > 0:
                result = monteCarlo0INF(lambda x: (x > a) * distr_fun(*args, x), N)
            else:
                r1 = monteCarlo0INF(lambda x: distr_fun(*args, x), N)
                r2 = monteCarloAB(lambda x: distr_fun(*args, x), a, 0, N)
                result = r1 + r2
            print(f'{N} iterations: P(X > a) = {result}')
        else:
            result = monteCarloAB(lambda x: distr_fun(*args, x), a, b, N)
            print(f'{N} iterations: P(a < X < b) = {result}')
