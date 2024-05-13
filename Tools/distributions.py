import math

def binomialProb(n, p, i):
    return math.comb(n, i) * (p**i) * ((1-p)**(n-i))
