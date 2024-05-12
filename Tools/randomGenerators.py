from random import random
import math
import graph

# Discrete variables

# Generic inverse transform method for X
# x: array of X possible values
# p: array of probabilities
def inverseTransformDVA(x, p):
    U = random()
    i, F = 0, p[0]
    while U >= F:
        i += 1
        F += p[i]
    return x[i]


# Uniform (discrete) distribution: X ~ U[a, b]
def uniformDVA(a, b):
    assert b >= a, 'Invalid bounds!'
    U = random()
    return int(U * (b-a + 1)) + a


# Geometric distribution: X ~ Geom(p)
def geometricVA(p):
    assert 0 <= p <= 1, 'Invalid value of p!'
    U = random()
    return int(math.log(1-U) / math.log(1-p)) + 1


# Bernoulli distribution: X ~ B(p)
def bernoulliVA(p):
    assert 0 <= p <= 1, 'Invalid value of p!'
    U = random()
    return U < p


# Poisson distribution: X ~ P(lamb)
# Non-optimized version
def poissonVA(lamb):
    U = random()
    i, p = 0, math.e ** (-lamb)
    F = p
    while U >= F:
        i += 1
        p *= lamb / i
        F += p
    return i


# Optimized version (less comparissons)
def poissonOptimizedVA(lamb):
    assert lamb > 0
    
    p = math.e ** (-lamb)
    F = p

    # Look for expected value (p_[lamb])
    for j in range(1, int(lamb) + 1 ):
        p *= lamb / j
        F += p
    
    U = random()
    if U >= F:
        j = int(lamb) + 1
        while U >= F:
            p *= lamb / j
            F += p
            j += 1
        return j - 1
    else:
        j = int(lamb)
        while U < F:
            F -= p
            p *= j / lamb
            j -= 1
        return j + 1


# Binomial distribution: X ~ B(n, p)
def binomialVA(n, p):
    c = p / (1-p)
    prob = (1-p) ** n
    
    F = prob
    i = 0
    U = random()

    while U >= F:
        prob *= c * (n-i) / (i+1)
        F += prob
        i += 1
    
    return i

# Other functions

# Given an array a of length N, and a number r with 0 <= r <= N,
# returns a subset of length N of the array a with its elements
# randomly permutated.
def permutation(a, r=None):

    N = len(a)

    r = N if r == None else r
    assert r == None or 0 <= r <= N, 'Invalid value of r!'

    for j in range(N-1, N-1-r, -1):
        index = int((j+1) * random())
        a[j], a[index] = a[index], a[j]

    return a[N-r:]


# Given a function g and a number N > 0, it calculates the average S of the
# first N elements g(a_i) with i=1,...,N, using the Law of Large Numbers
# (LLN) and the Monte Carlo method using N_SIM iterations.
def averageLLN(g, N, N_SIM):
    sum = 0
    for _ in range(N_SIM):
        # Equivalent to uniformDiscrete(1, N)
        U = int(random() * N) + 1
        sum += g(U)
    # Note that Monte Carlo calculates S/N, so we
    # multiply the result by N to get S.
    return sum / N_SIM * N


if __name__ == '__main__':
    NVars = int(input('Input number of samples: '))
    assert NVars > 0, 'NVars should be a positive integer!'

    # Generic inverse transform
    x = [1, 2, 5]
    p = [0.1, 0.6, 0.3]
    
    x_vec = graph.generateDVA(NVars, inverseTransformDVA, *[x, p])
    graph.graphDVA(x_vec, title=f'Inverse Transform\nx={x}\np={p}')

    # Uniform distribution
    a = int(input('Input Uniform variable lower bound (a): '))
    b = int(input('Input Uniform variable upper bound (b): '))
    assert b > a, 'Invalid bounds!'

    x_vec = graph.generateDVA(NVars, uniformDVA, *[a, b])
    graph.graphDVA(x_vec, title=f'Uniform X ~ U[{a},{b}]')

    # Geometric distribution
    pG = float(input('Input Geometric variable probability (p): '))
    assert 0 <= pG <= 1

    x_vec = graph.generateDVA(NVars, geometricVA, *[pG])
    graph.graphDVA(x_vec, title=f'Geometric X ~ Geom({pG})')

    # Bernoulli distribution
    pB = float(input('Input Bernoulli variable probability (p): '))
    assert 0 <= pB <= 1

    x_vec = graph.generateDVA(NVars, bernoulliVA, *[pB])
    graph.graphDVA(x_vec, title=f'Bernoulli X ~ B({pB})')

    # Poisson distribution
    lamb = float(input('Input Poisson variable lambda: '))
    assert lamb > 0

    # Poisson distribution (non-optimized)
    x_vec = graph.generateDVA(NVars, poissonVA, *[lamb])
    graph.graphDVA(x_vec, title=f'Poisson X ~ P({lamb})  (non-optimized)')

    # Poisson distribution (optimized)
    x_vec = graph.generateDVA(NVars, poissonOptimizedVA, *[lamb])
    graph.graphDVA(x_vec, title=f'Poisson X ~ P({lamb})  (optimized)')

    # Binomial distribution
    n = int(input('Input Binomial variable n: '))
    pBin = float(input('Input Binomial variable probability (p): '))
    assert n > 0
    assert 0 <= pBin <= 1

    x_vec = graph.generateDVA(NVars, binomialVA, *[n, pBin])
    graph.graphDVA(x_vec, title=f'Binomial X ~ B({n},{pBin})')
