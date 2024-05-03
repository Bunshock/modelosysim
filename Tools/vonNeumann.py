def vonNeumann(seed, n):
    u = seed
    for i in range(n):
        print(f'{i}: {u}')
        u = ((u ** 2) // 100) % 10000


if __name__ == "__main__":
    seed = int(input('Enter seed: '))
    n = int(input('Iterations: '))
    vonNeumann(seed, n)
