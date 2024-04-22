from random import random
import math

N_SIM = 100_000


# Simulation: v.a. N counts the ammount of numbers
# generated until their multiplication is bigger than
# e^(-3)
def simulation():
    mult, count = random(), 1
    while mult >= (math.e ** (-3)):
        mult *= random()
        count += 1
    return count


# E[N]:
sum = 0
for _ in range(N_SIM):
    X = simulation()
    sum += X

print(f'Estimated value of E[N]: {sum / N_SIM}')

# We want to calculate P(max{Ni}=n)
for n in range(7):
    count = 0
    for _ in range(N_SIM):
        X = simulation()
        if X == n:
            count += 1

    print(f'P(N={n}): {count / N_SIM}')
