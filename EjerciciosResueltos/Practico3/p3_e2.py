import random

N_SIM = 1_000_000


def simulation():
    U = random.uniform(0, 1)
    X = random.uniform(0, 1) + random.uniform(0, 1)
    if U >= 0.5:
        X += random.uniform(0, 1)
    return X


count = 0
for _ in range(N_SIM):
    X = simulation()

    # We want to calculate P(X >= 1), so
    # we count the number of times the v.a.
    # is bigger or equal than 1
    if X >= 1:
        count += 1

prob = count / N_SIM
print(f'({N_SIM} iterations) P(X >= 1) = {prob}')
