from Tools.randomGenerators import poissonOptimizedVA, poissonVA

# Calcular P(Y > 2) con Y ~ Poisson(10). Usar 10_000 iteraciones
# Recordemos que P(Y > 2) = 1 - P(Y <= 2)
N_SIM = 10_000

# Metodo no optimizado:
count_NO = 0
for _ in range(N_SIM):
    Y = poissonVA(10)
    if Y <= 2:
        count_NO += 1
print(f'Usando version no optimizada: P(Y > 2) = {count_NO / N_SIM}')

# Metodo optimizado:
count_O = 0
for _ in range(N_SIM):
    Y = poissonOptimizedVA(10)
    if Y <= 2:
        count_O += 1
print(f'Usando version optimizada: P(Y > 2) = {count_O / N_SIM}')
