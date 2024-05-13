from random import random
import math


# Transformada inversa de exp(lamb)
# Recordar: la media de la exponencial es 1/lamb
def exponencial(lamb):
    return -math.log(1-random()) / lamb


# a) Generacion de variable compuesta por varias funciones
# cada una con distintas probabilidades
# f_arr: arreglo de funciones, donde cada elemento es un arreglo
# [probabilidad, funcion, *argumentos]
def generarComp(f_arr):
    U = random()
    i, F = 0, f_arr[0][0]
    while U >= F:
        i += 1
        F += f_arr[i][0]
    return f_arr[i][1](f_arr[i][2])


# b) Generar datos usando tres exponenciales con medias 3, 5, 7 y
# probabilidades 0.5, 0.3, 0.2. Calcular la esperanza exacta y compararla
# con estimaciones usando 10_000 simulaciones
f_arr = [
    [0.5, exponencial, *[1/3]],
    [0.3, exponencial, *[1/5]],
    [0.2, exponencial, *[1/7]],
]

N_SIM = 10_000
sum = 0
for _ in range(N_SIM):
    X = generarComp(f_arr)
    sum += X

print(f'Valor exacto de E[X]: 4.40')
print(f'Valor estimado de E[X] ({N_SIM} simulaciones): {(sum / N_SIM):.4f}')
