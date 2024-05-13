from random import random


# Queremos generar X con f.p.m dada por
def p(i):
    return (0.5 ** (i+1)) + 0.25 * ((2/3) ** i)


# a) Generamos X usando el metodo de transformada inversa
def generarX_TI():
    U = random()
    i, F = 1, p(1)
    while U >= F:
        i += 1
        F += p(i)
    return i


# b) Estimar E[X] usando 10_000 iteraciones
N_SIM = 10_000
sum = 0
for _ in range(N_SIM):
    X = generarX_TI()
    sum += X
print(f'E[X] ({N_SIM} iterations): {(sum / N_SIM):.4f}')

print('Exact value of E[X] is: 2.5')
