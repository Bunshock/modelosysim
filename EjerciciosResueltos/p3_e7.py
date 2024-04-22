from random import random

N_SIM = 100_000


# Simulation: v.a. N counts the ammount of numbers
# generated until their sum is bigger than 1
def simulation():
    sum, count = 0, 0
    while sum <= 1:
        sum += random()
        count += 1
    return count


# We want to know the estimated value of N
sum = 0
for _ in range(N_SIM):
    X = simulation()
    sum += X

print(f'Estimated value of E[N]: {sum / N_SIM}')
