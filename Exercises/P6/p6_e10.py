from numpy import e, random as npRandom

# Datos observados
muestra = [86.0, 133.0, 75.0, 22.0, 11.0, 144.0, 78.0, 122.0, 8.0, 146.0, 33.0, 41.0, 99.0]
muestra.sort()

N = len(muestra)

# Hipotesis nula:
# H_0) Los numeros provienen de una distribucion exp. con media 50

# Test de Kolmogorov-Smirnov para datos continuos:
# Primero calculamos el estadistico (d_observado), para ello, necesitamos la distribucion
# F de la cual suponemos provienen los datos (exp(1/50))
def F(x):
    return 1 - e ** (-0.02*x)

D1 = [(j+1)/N - F(Y) for j, Y in enumerate(muestra)]
D2 = [F(Y) - j/N for j, Y in enumerate(muestra)]
d_obs = max(D1 + D2)

print(f'd_observado = {d_obs}')

# Ahora, estimamos el p-valor con N_SIM simulaciones
pvalor = 0
N_SIM = 10_000
for _ in range(N_SIM):
    # Generamos N uniformes (ver teorema)
    uniformes = npRandom.uniform(0, 1, N)
    uniformes.sort()
    # En cada iteracion, calculamos el estadistico para la muestra generada
    d_j = 0
    for j in range(N):
        u_j = uniformes[j]
        d_j = max(d_j, (j+1)/N - u_j, u_j - j/N)
    # Si el estadistico simulado es mayor al observado, contarlo
    if d_j >= d_obs:
        pvalor += 1
# Imprimimos el p-valor
print(f'p-valor = {pvalor / N_SIM}')
