from scipy.stats import chi2
from random import random


# a)
areas = [31, 22, 12, 10, 8, 6, 4, 4, 2, 1]
NF = [188, 138, 87, 65, 48, 32, 30, 34, 13, 2]
N = sum(NF)

print(f'Areas: {areas}')
print(f'Observaciones: {NF}')
print(f'Cantidad de observaciones: {N}')

# b)
# H0) La rueda es justa. Es decir, la probabilidad de obtener
# el premio i es p(i) = probs[i], donde
probs = [area / 100.0 for area in areas]

# c)
t_obs = 0
for i in range(10):
    p_i = areas[i] / 100.0
    t_obs += ((NF[i] - N*p_i) ** 2) / (N*p_i)
print(f't_observado = {t_obs}')

# d)
chi2Fun = chi2(9)
pvalor_chi = chi2Fun.sf(t_obs)
print(f'p-valor usando chi-cuadrado: {pvalor_chi}')


# Generar valores entre 1 y 10 incluidos con las probabilidades
# dadas en las areas de la rueda
def generarX():
    U = random()
    i, F = 0, probs[0]
    while U >= F:
        i += 1
        F += probs[i]
    return i+1


# Simulamos el p-valor con N_SIM simulaciones
pvalor = 0
N_SIM = 1_000
for _ in range(N_SIM):
    muestra_j = []
    for _ in range(N):
        muestra_j.append(generarX())
    NF = [muestra_j.count(i+1) for i in range(10)]
    t_j = 0
    for i in range(10):
        p_i = probs[i]
        t_j += ((NF[i] - N*p_i) ** 2) / (N*p_i)
    if t_j >= t_obs:
        pvalor += 1

print(f'p-valor ({N_SIM} simulaciones): {pvalor / N_SIM}')
