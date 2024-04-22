"""
Un supermercado posee 3 cajas. Los clientes se dirigen a cada caja:
40% --> caja 1,  32% --> caja 2,  28% --> caja 3
El tiempo que espera una persona para ser atendido en cada caja:
caja 1 ~ exp(1/3),  caja 2 ~ exp(1/4),  caja 3 ~ exp(1/5)

La probabilidad de que el tiempo de espera de un cliente sea menor
a 4 minutos es
P(X < 4) = P(X1 < 4) * 0.4 + P(X2 < 4) * 0.32 + P(X3 < 4) * 0.28
         = 0.651

Dado que el tiempo de espera de un cliente es mayor a 4 minutos,
la probabilidad de que haya elejido la caja:
    1: es: P(caja 1 | X > 4) = 0.8440
    2: es: P(caja 2 | X > 4) = 0.5796
    3: es: P(caja 3 | X > 4) = 0.4418

Para simular: Cada simulacion crea un cliente y le asigna,
dependiendo de una variable aleatoria uniforme en (0, 1),
la caja correspondiente:
Si    0 <= U < 0.4,  asigno caja 1
Si  0.4 <= U < 0.72, asigno caja 2
Si 0.72 <= U < 1,    asigno caja 3
Luego, hago esperar a cada una de estas personas dependiendo
de la distribucion exponencial correspondiente
Si el tiempo de espera es menor que 4, entonces lo agrego a la
cuenta.
"""

import random

N_SIM = 1_000_000


def simulation():
    U = random.random()
    if U < 0.4:
        wait_time = random.expovariate(1/3.0)
    elif U >= 0.4 and U < 0.72:
        wait_time = random.expovariate(1/4.0)
    else:
        wait_time = random.expovariate(1/5.0)
    return wait_time


count = 0
for _ in range(N_SIM):
    X = simulation()
    if X < 4:
        count += 1

prob = count / N_SIM
print(f'P(X < 4) = {prob}')
