"""
Sean X1 y X2 las variables aleatorias discretas (uniformes)
que devuelven el resultado de tirar un dado legal.
Luego X1 ~ U[1,6] y X2 ~ U[1,6]
Ahora, si sumamos los valores de X1 y X2, entonces
X = X1 + X2 tiene distribucion de la convolucion X1 * X2:
P(X = i) = sum(x) (pX1(x)pX2(i-x))  , con i=2,...,12
         = (1/6) * ( sum(x=1 to 6) 1/6  , si 1 <= i-x <= 6 )

Ejemplo: P(X = 2):
    (1/6) * [
          (x=1: i-x = 2-1 = 1 y 1 <= i-x = 1 <= 6) (1/6)
        + (x=2: i-x = 2-2 = 0 y 0 < 1) 0
        + (...)
        + (x=6: i-x = 2-6 = -4 y -4 < 1) 0
    ]
    = (1/6) * [1/6] = 1/36

Queremos simular el evento: Tirar los dados hasta que todos
los resultados posibles hayan salido (1,...,12)
"""
from random import random

def simulation():
    gotResult = [1] * 12
    sum = 12
    throws = 0
    while sum > 0:
        # Throw both dices
        X = int(random() * 6) + 1
        Y = int(random() * 6) + 1
        
        result = X + Y

        if gotResult[result - 1]:
            gotResult[result - 1] -= 1
            sum -= 1

        throws += 1

    return throws

N_SIM = 10
throws_sum = 0
for _ in range(N_SIM):
    X = simulation()
    throws_sum += X
throws_avg = throws_sum / N_SIM
print(throws_avg)