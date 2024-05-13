from Tools.randomGenerators import generateDVA
from Tools.graph import graphDVA
from random import random
import numpy as np


def QueDevuelve(p1, p2):
    X = int(np.log(1-random())/np.log(1-p1))+1
    Y = int(np.log(1-random())/np.log(1-p2))+1
    return min(X, Y)

"""
Sabiendo que X ~ Geom(p1) e Y ~ Geom(p2), podemos calcular que distribucion
tiene min(X, Y). Planteamos la distribucion acumulada P(min(X, Y) <= j) y,
resolviendo, llegamos a que F_{min(X,Y)} (j) = 1 - (q1*q2)^(j-1)
que es la funcion de distribucion acumulada para una variable aleatoria
geometrica con parametro 1-q1*q2, donde q1 = 1-p1 y q2 = 1-p2
Por lo tanto, min(X,Y) ~ Geom(1-q1*q2)
"""

N_SIM = 10_000
# Generamos una Geom(1-0.8*0.5) = Geom(1-0.4) = Geom(0.6)
x_vec = generateDVA(N_SIM, QueDevuelve, *[0.2, 0.5])
graphDVA(x_vec, N_SIM, title='QueDevuelve(0.2, 0.5) ~ Geom(0.6)')


"""
Escriba otro algoritmo que utilice un único número aleatorio (random()) y que
simule una variable con la misma distribución que la simulada por 
QueDevuelve(0.05, 0.2)
"""
def QueDevuelve2(p1, p2):
    U = random()
    p = 1 - (1-p1) * (1-p2)
    count = 0
    while U >= p:
        U = random()
        count += 1
    return count

# Comparamos ambas funciones:
x_vec = generateDVA(N_SIM, QueDevuelve, *[0.05, 0.2])
graphDVA(x_vec, N_SIM, title='QueDevuelve(0.05, 0.2) ~ Geom(0.24)')

x_vec = generateDVA(N_SIM, QueDevuelve2, *[0.05, 0.2])
graphDVA(x_vec, N_SIM, title='QueDevuelve(0.05, 0.2) ~ Geom(0.24)')
