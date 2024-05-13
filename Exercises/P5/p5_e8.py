from random import random
import math


# Funcion densidad de X
def densidadX(x):
    if x < 0 or x >= 2: return 0
    elif x < 1: return x
    else: return 2 - x


# b) Generar X
# (i) Usando que X es suma de dos uniformes U, V ~ U(0, 1)
def generarX_suma():
    U = random()
    V = random()
    return U + V

# (ii) Metodo de transformada inversa
def generarX_TI():
    U = random()
    if U < 0.5: return math.sqrt(2*U)
    else: return 2 - math.sqrt(2) * math.sqrt(1-U)

# (iii) Metodo de rechazo. Rechazamos una Y ~ U(0, 2)
# Elijo  c >= densidad(x) / 0.5 >= max(densidad(x)) / 0.5
# Luego, c >= densidadX(1) / 0.5 = 2. Tomo c = 2
def generarX_AyR():
    while True:
        Y = random() * 2
        U = random()
        c = 2
        if U <= densidadX(Y) / (c * 0.5):
            return Y


# c) Comparar eficiencias, estimando el valor esperado promediando
# 10_000 valores simulados
print('c)')

N_SIM = 10_000
sum_S, sum_TI, sum_AyR = 0, 0, 0
for _ in range(N_SIM):
    X1 = generarX_suma()
    sum_S += X1

    X2 = generarX_TI()
    sum_TI += X2

    X3 = generarX_AyR()
    sum_AyR += X3

print(f'E[X] usando suma de uniformes ({N_SIM} simulaciones): {sum_S / N_SIM}')
print(f'E[X] usando Transformada Inversa ({N_SIM} simulaciones): {sum_TI / N_SIM}')
print(f'E[X] usando Aceptacion y rechazo ({N_SIM} simulaciones): {sum_AyR / N_SIM}')


# Para que valor x0 se cumple que P(X > x0) = 0.125?
# Resolviendo, obtenemos x0 = 1.5
# d) Comparamos el valor anterior con simulaciones
print('d)')

count_S, count_TI, count_AyR = 0, 0, 0
for _ in range(N_SIM):
    X1 = generarX_suma()
    if X1 > 1.5:
        count_S += 1

    X2 = generarX_TI()
    if X2 > 1.5:
        count_TI += 1

    X3 = generarX_AyR()
    if X3 > 1.5:
        count_AyR += 1

print(f'Suma de uniformes ({N_SIM} simulaciones): P(X > 1.5) = {count_S / N_SIM}')
print(f'Transformada Inversa ({N_SIM} simulaciones): P(X > 1.5) = {count_TI / N_SIM}')
print(f'Aceptacion y Rechazo ({N_SIM} simulaciones): P(X > 1.5) = {count_AyR / N_SIM}')
