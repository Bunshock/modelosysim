from random import random
import math

"""
Implementamos un algoritmo que calcula el numero de eventos
'NT' y sus tiempos de arribo 'Eventos' en las primeras 'T'
unidades de tiempo de un proceso de Poisson homogeneo de 
parametro 'lamb'.
"""
def eventosPoisson(lamb, T):
    t, NT = 0, 0
    Eventos = []
    while t < T:
        U = 1 - random()

        # Simulamos el proximo tiempo de arribo: exp(lamb)
        t += - math.log(U) / lamb

        # Si no me pase de T, entonces cuento el evento
        if t <= T:
            NT += 1
            Eventos.append(t)

    return NT, Eventos


# Probamos el generador:
# Dado un proceso de Poisson de parametro lambda = 1.4,
# Calculamos P(N(5) <= 3) = 0.081765:
count = 0
N_SIM = 10_000
for _ in range(N_SIM):
    NT, _ = eventosPoisson(1.4, 5)
    if NT <= 3:
        count += 1

print(f'Valor estimado ({N_SIM} simulaciones) de P(N(5) <= 3) = {count / N_SIM}')
