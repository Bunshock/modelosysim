from random import random
import Tools.graph as graph

# X takes values i in {1,...,10} with probabilities p[i]:
p = [0.11, 0.14, 0.09, 0.08, 0.12, 0.10, 0.09, 0.07, 0.11, 0.09]

N_SIM = 10_000

# a) Aceptacion y Rechazo with uniform Y ~ U[1, 10]
# c parameter is: 0.14 / 0.1 = 1.4
def AyR():
    while True:
        Y = int(random() * 10) + 1
        U = random()
        if U <= p[Y-1] / (1.4 * 0.1):
            return Y

x_vec = graph.generateDVA(N_SIM, AyR, *[])
graph.graphDVA(x_vec, title='Aceptacion y Rechazo')


# b) Metodo de la transformada inversa
def transformadaInversa():
    U = random()
    i, F = 1, p[0]
    while U >= F:
        i += 1
        F += p[i-1]
    return i

x_vec = graph.generateDVA(N_SIM, transformadaInversa, *[])
graph.graphDVA(x_vec, title='Transformada inversa')


# c) Metodo de la urna (k = 100)
k = 100
urna = []
for i in range(10):
    urna += [i] * int(p[i]*k)

def metodoUrna():
    U = int(random() * 100)
    return urna[U]
    
x_vec = graph.generateDVA(N_SIM, metodoUrna, *[])
graph.graphDVA(x_vec, title='Metodo de la urna')
