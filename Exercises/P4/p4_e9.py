from Tools.randomGenerators import geometricRecVA, generateDVA
from Tools.timeEfficiency import timeEfficiency
from random import random


N_SIM = 10_000
N_TIME_CHECKS = 100

# Valores teoricos
print('Theorical values:')
print('X ~ Geom(0.8):    E[X] = 1.25')
print('X ~ Geom(0.2):    E[X] = 5.00')


# a) Transformada inversa usando formula recursiva
print('a)')

geomI = geometricRecVA

# p = 0.8
timeI = 0
for _ in range(N_TIME_CHECKS):
    x_vec, time_elapsed = timeEfficiency(generateDVA, *[N_SIM, geomI, *[0.8]])
    timeI += time_elapsed
print('Results from geomI (inverse transform method with recursive formula) with p=0.8')
print(f'Time efficiency ({N_SIM} iterations): {(timeI / N_TIME_CHECKS * 1000):.4f} ms')
print(f'Estimated value of E[X]: {sum(x_vec) / N_SIM}')

# p = 0.2
timeI = 0
for _ in range(N_TIME_CHECKS):
    x_vec, time_elapsed = timeEfficiency(generateDVA, *[N_SIM, geomI, *[0.2]])
    timeI += time_elapsed
print('Results from geomI (inverse transform method with recursive formula) with p=0.2')
print(f'Time efficiency ({N_SIM} iterations): {(timeI / N_TIME_CHECKS * 1000):.4f} ms')
print(f'Estimated value of E[X]: {sum(x_vec) / N_SIM}')


# b) Simulando ensayos con probabilidad de exito p hasta
# obtener un exito
print('b)')

def geomII(p):
    count = 1
    while random() > p:
        count += 1
    return count

timeII = 0
for _ in range(N_TIME_CHECKS):
    x_vec, time_elapsed = timeEfficiency(generateDVA, *[N_SIM, geomII, *[0.8]])
    timeII+= time_elapsed
print('Results from geomII (simulate until success) with p=0.8')
print(f'Time efficiency ({N_SIM} iterations): {(timeII / N_TIME_CHECKS * 1000):.4f} ms')
print(f'Estimated value of E[X]: {sum(x_vec) / N_SIM}')

timeII = 0
for _ in range(N_TIME_CHECKS):
    x_vec, time_elapsed = timeEfficiency(generateDVA, *[N_SIM, geomII, *[0.2]])
    timeII+= time_elapsed
print('Results from geomII (simulate until success) with p=0.2')
print(f'Time efficiency ({N_SIM} iterations): {(timeII / N_TIME_CHECKS * 1000):.4f} ms')
print(f'Estimated value of E[X]: {sum(x_vec) / N_SIM}')
