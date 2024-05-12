from Tools.randomGenerators import binomialVA, bernoulliVA, generateDVA
from Tools.timeEfficiency import timeEfficiency

# Implementar una binomial Bin(n, p)

# (I) Usando transformada inversa
binI = binomialVA

# (II) Simulando n ensayos con probabilidad de exito p y contando el numero de exitos
def binII(n, p):
    count = 0
    for _ in range(n):
        X = bernoulliVA(p)
        count += X
    return count

# a) Comparar eficiencias para n=10, p=0.3; con 10_000 simulaciones
print('a)')

N_SIM = 10_000
N_TIME_CHECKS = 100

timeI = 0
for _ in range(N_TIME_CHECKS):
    _, time_elapsed = timeEfficiency(generateDVA, *[N_SIM, binI, *[10, 0.3]])
    timeI += time_elapsed
print(f'Time efficiency of binI ({N_SIM} iterations): {(timeI / N_TIME_CHECKS * 1000):.4f} ms')

timeII = 0
for _ in range(N_TIME_CHECKS):
    _, time_elapsed = timeEfficiency(generateDVA, *[N_SIM, binII, *[10, 0.3]])
    timeII += time_elapsed
print(f'Time efficiency of binII ({N_SIM} iterations): {(timeII / N_TIME_CHECKS * 1000):.4f} ms')

print(f'\nProportionally, binII is {(timeII / timeI):.4f} times slower than binI')

# b) Estimar el valor con mayor ocurrencia de cada implementacion y la proporcion de veces
# que se obtuvieron los valores 0 y 10
print('\nb)')

estimatedI = 0
countI_0, countI_10 = 0, 0
for _ in range(N_SIM):
    X = binI(10, 0.3)
    if X == 0:
        countI_0 += 1
    elif X == 10:
        countI_10 += 1
    estimatedI += X
print((
    f'Estimated value of binI ({N_SIM} iterations): {estimatedI / N_SIM}\n'
    f'Proportion of times we got value 0: {countI_0 / N_SIM}\n'
    f'Proportion of times we got value 10: {countI_10 / N_SIM}'
))

print('')

estimatedII = 0
countII_0, countII_10 = 0, 0
for _ in range(N_SIM):
    X = binII(10, 0.3)
    if X == 0:
        countII_0 += 1
    elif X == 10:
        countII_10 += 1
    estimatedII += X
print((
    f'Estimated value of binII ({N_SIM} iterations): {estimatedII / N_SIM}\n'
    f'Proportion of times we got value 0: {countII_0 / N_SIM}\n'
    f'Proportion of times we got value 10: {countII_10 / N_SIM}'
))


# c)
print('c)\nIn theory:')
print('Estimated value:         E[X] = np = 10 * 0.3 = 3')
print('Proportion of values 0:  P(X = 0)  = 0.0282475')
print('Proportion of values 10: P(X = 10) = 0.0000059')
