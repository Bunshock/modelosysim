from random import random


# a) Generamos X con distribucion de Cauchy de parametro lambda
def generarCauchy(lamb):
    while True:
        U1 = random()
        U2 = random()
        Z = (2 * U1 - 1) / U2
        if U1 ** 2 < 1 / (1 + Z ** 2):
            return Z * lamb


# d) Calcular P(-lambda < X < lambda) para lambda = 1, 2.5, 0.3
N_SIM = 10_000
count_I, count_II, count_III = 0, 0, 0
for _ in range(N_SIM):
    X1 = generarCauchy(1)
    if -1 < X1 < 1:
        count_I += 1

    X2 = generarCauchy(2.5)
    if -2.5 < X2 < 2.5:
        count_II += 1
    
    X3 = generarCauchy(0.3)
    if -0.3 < X3 < 0.3:
        count_III += 1


print('\nValor real (lambda = 1) de P(-1 < X < 1) = 0.5')
print((
    f'Valor estimado (lambda = 1) ({N_SIM} simulaciones) de P(-1 < X < 1) = '
    f'{count_I / N_SIM}'
))
print('\nValor real (lambda = 2.5) de P(-2.5 < X < 2.5) = 0.5')
print((
    f'Valor estimado (lambda = 2.5) ({N_SIM} simulaciones) de P(-2.5 < X < 2.5) = '
    f'{count_II / N_SIM}'
))
print('\nValor real (lambda = 0.3) de P(-0.3 < X < 0.3) = 0.5')
print((
    f'Valor estimado (lambda = 0.3) ({N_SIM} simulaciones) de P(-0.3 < X < 0.3) = '
    f'{count_III / N_SIM}'
))
