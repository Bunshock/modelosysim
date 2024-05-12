from random import random
import Tools.graph as graph
from Tools.timeEfficiency import timeEfficiency

# X takes values i in {1,...,10} with probabilities p[i]:
p = [0.11, 0.14, 0.09, 0.08, 0.12, 0.10, 0.09, 0.07, 0.11, 0.09]

N_SIM = 10_000
N_TIME_CHECKS = 100

# a) Aceptacion y Rechazo with uniform Y ~ U[1, 10]
# c parameter is: 0.14 / 0.1 = 1.4
def AyR():
    while True:
        Y = int(random() * 10) + 1
        U = random()
        if U <= p[Y-1] / (1.4 * 0.1):
            return Y

# Calculate time efficiency for this method
time_AyR = 0
for _ in range(N_TIME_CHECKS):
    x_vec, time_elapsed = timeEfficiency(graph.generateDVA, *[N_SIM, AyR, *[]])
    time_AyR += time_elapsed
print(f'Time efficiency of AyR ({N_SIM} iterations): {(time_AyR / N_TIME_CHECKS * 1000):.4f} ms')

# Graph only the last one generated
graph.graphDVA(x_vec, N_SIM, title='Aceptacion y Rechazo')


# b) Metodo de la transformada inversa
def transformadaInversa():
    U = random()
    i, F = 1, p[0]
    while U >= F:
        i += 1
        F += p[i-1]
    return i

# Calculate time efficiency for this method
time_TI = 0
for _ in range(N_TIME_CHECKS):
    x_vec, time_elapsed = timeEfficiency(graph.generateDVA, *[N_SIM, transformadaInversa, *[]])
    time_TI += time_elapsed
print(f'Time efficiency of Transformada Inversa ({N_SIM} iterations): {(time_TI / N_TIME_CHECKS * 1000):.4f} ms')

# Graph only the last one generated
graph.graphDVA(x_vec, N_SIM, title='Transformada inversa')


# c) Metodo de la urna (k = 100)
k = 100
urna = []
for i in range(10):
    urna += [i] * int(p[i]*k)

def metodoUrna():
    U = int(random() * 100)
    return urna[U]

# Calculate time efficiency for this method
time_urna = 0
for _ in range(N_TIME_CHECKS):
    x_vec, time_elapsed = timeEfficiency(graph.generateDVA, *[N_SIM, metodoUrna, *[]])
    time_urna += time_elapsed
print(f'Time efficiency of urna ({N_SIM} iterations): {(time_urna / N_TIME_CHECKS * 1000):.4f} ms')

# Graph only the last one generated
graph.graphDVA(x_vec, N_SIM, title='Metodo de la urna')
