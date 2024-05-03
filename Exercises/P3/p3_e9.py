import random

N_SIM = 10


def simulation():
    X1 = random.randint(1, 6)
    if X1 == 1 or X1 == 6:
        return 2 * random.randint(1, 6)
    else:
        return random.randint(1, 6) + random.randint(1, 6)


wins = 0
for _ in range(N_SIM):
    score = simulation()
    if score > 6:
        wins += 1

prob_win = wins / N_SIM
print(f'Win probability is: {prob_win}')