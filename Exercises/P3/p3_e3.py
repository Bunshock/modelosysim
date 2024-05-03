import random

N_SIM = 1_000_000


def simulation():
    U = random.random()
    X = random.random() + random.random()
    if U >= (1 / 3.0):
        X += random.random()
    return X


count = 0
for _ in range(N_SIM):
    X = simulation()
    if X <= 2:
        count += 1

prob = count / N_SIM
print(f'({N_SIM} iterations) P(X <= 2) = {prob}')
