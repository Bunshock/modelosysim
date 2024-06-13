import math
from random import random

muestra = [1.6, 10.3, 3.5, 13.5, 18.4, 7.7, 24.3, 10.7, 8.4, 4.9, 7.9, 12, 16.2, 6.8, 14.7]
muestra.sort()
n = len(muestra)

_lambda_estimado = n / sum(muestra)
print(f'lambda estimado: {_lambda_estimado}')

def F(x, lamb):
    return 1 - math.e ** (-lamb * x)

d_observado = 0
for j in range(n):
    F_j = F(muestra[j], _lambda_estimado)
    d_observado = max(d_observado, (j+1)/n - F_j, F_j - j/n)
print(f'd_observado: {d_observado}')

def generarExp(lamb):
    return -math.log(1-random()) / lamb


pvalor = 0
N_SIM = 1_000
for _ in range(N_SIM):
    # Generamos muestra de n exponenciales de parametro
    # _lambda_estimado
    muestra_j = []
    for _ in range(n):
        muestra_j.append(generarExp(_lambda_estimado))
    muestra_j.sort()
    # Estimamos lambda con nueva muestra
    _lambda_j = n / sum(muestra_j)
    # Calculamos el estadistico d para esta muestra
    d_j = 0
    for j in range(n):
        F_j = F(muestra_j[j], _lambda_j)
        d_j = max(d_j, (j+1)/n - F_j, F_j - j/n)
    # Contamos si d_j >= d_observado
    if d_j >= d_observado:
        pvalor += 1

print(f'p-valor ({N_SIM} simulaciones): {pvalor / N_SIM}')
