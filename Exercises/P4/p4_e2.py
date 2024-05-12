from random import random
from Tools.randomGenerators import averageLLN
import math

N = 10_000

def g(x):
    return math.e ** (x/N)


# Calculate sum from i=1 to N of g(i) using
# LLN and Monte Carlo theory
N_SIM = 100
sum = 0
for _ in range(N_SIM):
    # U is a random value taken from U ~ U[1, 10_000]
    U = int(random() * N) + 1
    sum += g(U)
sum = sum / N_SIM * N


print(f'b) Aproximate sum, 100 iterations: {sum}')


def sumOfFirstM(M, g):
    sum = 0
    for i in range(M+1):
        sum += g(i+1)
    return sum


print(f'c) Sum of first 100 terms: {sumOfFirstM(100, g)}')
