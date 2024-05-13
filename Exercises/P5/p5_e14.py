"""
Los autobuses que llevan los aficionados a un encuentro deportivo llegan a
destino de acuerdo con un proceso de Poisson a razón de cinco por hora.
La capacidad de los autobuses es una variable aleatoria que toma valores en
el conjunto: {20,21,...,40} con igual probabilidad. A su vez, las capacidades
de dos autobuses distintos son variables independientes. Escriba un algoritmo
para simular la llegada de aficionados al encuentro en el instante t = 1hora.
"""

"""
Arribo de aficionados: Proceso de Poisson con lambda = 5 (en horas)
Capacidad del autobus: U ~ U[20, 40]
Entonces, simulamos un proceso de Poisson con lambda = 5 para T=1
y, en cada arribo, en vez de contar 1 evento, contamos una variable
uniforme U[20, 40], es decir, vamos sumando la cantidad de
aficionados que llegan al evento.
"""
from random import random
import math

def aficionadosPoisson(lamb, T):
    t, NT = 0, 0
    while t < T:
        U = 1 - random()

        # Simulamos el proximo tiempo de arribo: exp(lamb)
        # del proximo autobus
        t += - math.log(U) / lamb

        # Si no me pase de T, entonces sumo la cantidad de
        # aficionados que llegaron, una uniforme U[20, 40]
        if t <= T:
            NT += int(random() * (40-20 + 1)) + 20

    return NT

# Simulamos P(Numero de aficionados en t=1 > 65) con 10_000 iteraciones
N_SIM = 10_000
count = 0
for _ in range(N_SIM):
    aficionados = aficionadosPoisson(5, 1)
    if aficionados > 65:
        count += 1

print((
    'La probabilidad estimada de que la cantidad de aficionados en t = 1 hora '
    f'sea mayor que 65 es: {(count / N_SIM):.5f}'
))