from random import random
import math


# Generacion de variable aleatoria normal X ~ N(mu, sig)

# a) Mediante generación de variables exponenciales según el 
# ejemplo 5f del libro Simulacion de S. M. Ross
def generarNormal_Exp(mu, sig):
    while True:
        # Generamos dos variables con distribucion exp(1)
        Y1 = - math.log(random())
        Y2 = - math.log(random())
        if Y2 - ((Y1-1)**2) / 2 > 0:
            U = random()
            if U < 0.5:
                return Y1 * sig + mu
            else:
                return -Y1 * sig + mu

# b) Metodo polar (devuelve 2 normales)
def generarNormal_Polar(mu, sig):
    RCuadrado = -2 * math.log(1 - random())
    Theta = 2 * math.pi * random()
    X = math.sqrt(RCuadrado) * math.cos(Theta)
    Y = math.sqrt(RCuadrado) * math.sin(Theta)
    return (X * sig + mu, Y * sig + mu)

# c) Metodo de razon entre uniformes
def generarNormal_RazonU(mu, sig):
    while True:
        U1 = random()
        U2 = random()
        Z = (4 * math.exp(-0.5) / math.sqrt(2.0)) * (U2 - 0.5) / U1
        if Z ** 2 < -4 * math.log(U1):
            return Z * sig + mu


# Comparamos midiendo la media muestral y la varianza con 10_000 simulaciones
N_SIM = 10_000
sum_E, sum_P, sum_R = 0, 0, 0
var_E, var_P, var_R = 0, 0, 0
for _ in range(N_SIM):
    X1 = generarNormal_Exp(0, 1)
    sum_E += X1
    var_E += X1 ** 2

    X2 = generarNormal_Polar(0, 1)[0]
    sum_P += X2
    var_P += X2 ** 2

    X3 = generarNormal_RazonU(0, 1)
    sum_R += X3
    var_R += X3 ** 2

print(f'E[X] usando exponenciales ({N_SIM} simulaciones): {sum_E / N_SIM}')
print(f'Var(X) usando exponenciales ({N_SIM} simulaciones): {(var_E - sum_E * sum_E / N_SIM) / (N_SIM - 1)}')
print('')
print(f'E[X] usando metodo polar ({N_SIM} simulaciones): {sum_P / N_SIM}')
print(f'Var(X) usando metodo polar ({N_SIM} simulaciones): {(var_P - sum_P * sum_P / N_SIM) / (N_SIM - 1)}')
print('')
print(f'E[X] usando razon de uniformes ({N_SIM} simulaciones): {sum_R / N_SIM}')
print(f'Var(X) usando razon de uniformes ({N_SIM} simulaciones): {(var_R - sum_R * sum_R / N_SIM) / (N_SIM - 1)}')
