from random import random


def generarX():
    U=random()
    if U<0.22:
       return 1
    elif U<0.55:
       return 2
    elif U<0.72:
       return 3
    elif U<0.9999:
       return 4
    else:
       return 100
    

N_SIM = 100_000
sum = 0
for _ in range(N_SIM):
   X = generarX()
   sum += X ** 2
print(f'E[X^2] = {sum / N_SIM}')
