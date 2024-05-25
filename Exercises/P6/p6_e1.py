from random import gauss
from math import sqrt

# Limitar iteraciones y prevenir loop infinito
N_SIM_MAX = 10_000_000

# Estimacion de E[X], Var(X) con error cuadratico medio ECM menor a d=0.1
# Donde X es una variable aleatoria normal estandar
d = 0.1
Media = gauss()
Scuad, n = 0, 1
while (n <= 100 or sqrt(Scuad/n) > d) and n <= N_SIM_MAX:
    n += 1
    # Simulamos X
    X = gauss()

    OldMedia = Media
    # Calculo de la media de forma recursiva
    Media = OldMedia + (X - OldMedia) / n
    # Calculo de la varianza de forma recursiva
    Scuad = Scuad * (1 - 1/(n-1)) + n * (Media - OldMedia) ** 2

print(f'Numero estimado de iteraciones (n): {n}')
print(f'Estimacion de la media: {Media}')
print(f'Estimacion de la varianza: {Scuad}')
