from random import random
from Tools.randomGenerators import binomialVA, generateDVA
from Tools.distributions import binomialProb
from Tools.timeEfficiency import timeEfficiency


# Probabilities vector
p = [0.15, 0.20, 0.10, 0.35, 0.20]


# I)
def generarX_TI():
    U = random()
    if U < 0.35: return 3
    elif U < 0.55: return 1
    elif U < 0.75: return 4
    elif U < 0.90: return 0
    else: return 2

# II)
def generarX_AyR():
    while True:
        Y = binomialVA(4, 0.45)
        U = random()
        if U < p[Y] / (4.87731 * binomialProb(4, 0.45, Y)):
            return Y

# III)
N_SIM = 10_000
N_TIME_CHECKS = 100

time_TI = 0
for _ in range(N_TIME_CHECKS):
    x_vec, time_elapsed = timeEfficiency(generateDVA, *[N_SIM, generarX_TI, *[]])
    time_TI += time_elapsed
print(f'Time efficiency of TI ({N_SIM} iterations): {(time_TI / N_TIME_CHECKS * 1000):.4f} ms')

time_AyR = 0
for _ in range(N_TIME_CHECKS):
    x_vec, time_elapsed = timeEfficiency(generateDVA, *[N_SIM, generarX_AyR, *[]])
    time_AyR += time_elapsed
print(f'Time efficiency of AyR ({N_SIM} iterations): {(time_AyR / N_TIME_CHECKS * 1000):.4f} ms')
