from random import random
import math

# Funcion densidad de probabilidad de X
def densidadX(x):
    return (1 <= x <= math.e) * (1 / x)



# a) Desarrollar metodos para generar X
"""
i) Transformada inversa: Integramos f de -inf a x
buscando F(x):

F(x) = | ln(x)  , si 1 <= x <= e 
       | 0      , c.c.

Luego, si U ~ U(0, 1), U = F(x) sii
U = ln(x) <=> x = e ** U
"""
def generarX_TI():
    return math.e ** random()

"""
ii) Aceptacion y Rechazo: rechazando una Y ~ U(1, e)
La funcion densidad de probabilidad de Y es:
"""
def densidadY(x):
    return (1 <= x <= math.e) * (1 / (math.e-1))

"""
Calculamos c, tal que densidadX(x) / densidadY(x) <= c
para todo x tal que densidadX(x) != 0
Luego, densidadX(x) / densidadY(x) = (e - 1) / x
Como x esta en (1, e), y el resultado anterior representa
una funcion decreciente, entonces el valor mayor va a estar
dado cuando x = 1. Luego c debe ser tal que
c >= e - 1. Tomo c = e - 1
"""
def generarX_AyR():
    while True:
        Y = random() * (math.e - 1) + 1
        U = random()
        c = math.e - 1
        if U <= densidadX(Y) / (c * densidadY(Y)):
            return Y


# b) Comparamos la eficiencia usando 10_000 simulaciones, 
# comparando los promedios de los valores obtenidos en cada
# metodo. Sabemos que E[X] = e - 1
print('b)')

N_SIM = 10_000

sum_TI, sum_AyR = 0, 0
for _ in range(N_SIM):
    X1 = generarX_TI()
    sum_TI += X1

    X2 = generarX_AyR()
    sum_AyR += X2

print(f'E[X] usando Transformada Inversa ({N_SIM} simulaciones): {sum_TI / N_SIM}')
print(f'E[X] usando Aceptacion y Rechazo ({N_SIM} simulaciones): {sum_AyR / N_SIM}')


# c) Calculamos P(X <= 2) usando ambos metodos
print('c)')

count_TI, count_AyR = 0, 0
for _ in range(N_SIM):
    X1 = generarX_TI()
    if X1 <= 2:
        count_TI += 1
    
    X2 = generarX_AyR()
    if X2 <= 2:
        count_AyR += 1

print(f'Transformada Inversa ({N_SIM} simulaciones): P(X <= 2) = {count_TI / N_SIM}')
print(f'Aceptacion y Rechazo ({N_SIM} simulaciones): P(X <= 2) = {count_AyR / N_SIM}')
