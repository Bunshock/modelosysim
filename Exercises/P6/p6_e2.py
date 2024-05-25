from random import random, gauss
from math import exp, sqrt

# Limitar iteraciones y prevenir loop infinito
N_SIM_MAX = 10_000_000
# Iteraciones para estimar usando el metodo de Monte Carlo usual
N_SIM = 10_000
# Limitador de la desviacion estandar muestral
d = 0.01


# Funcion para estimar el valor de una integral de una funcion g
# mediante el metodo de Monte Carlo, frenando cuando la desviacion
# estandar del estimador sea menor a d
# Para el caso de Monte Carlo fuera del intervalo (0, 1), definir
# g usando las transformaciones necesarias
def estimarIntegral(d, g):
    Integral = g(random())
    Scuad, n = 0, 1
    while (n <= 100 or sqrt(Scuad/n) > d) and n <= N_SIM_MAX:
        n += 1
        X = g(random())
        IntegralOld = Integral
        Integral = IntegralOld + (X - IntegralOld) / n
        Scuad = Scuad * (1 - 1/(n-1)) + n * (Integral - IntegralOld) ** 2
    return Integral, n, Scuad / n


# i)
print('i)')

def g_I(x):
    return exp(x) / sqrt(2*x)

print('a)')

# Metodo de Monte Carlo (intervalo (0,1)) con N simulaciones
def MonteCarlo01(g, N):
    integral = 0
    for _ in range(N):
        X = random()
        integral += g(X)
    return integral / N

print(f'Valor estimado usando Monte Carlo usual ({N_SIM} simulaciones): {MonteCarlo01(g_I, N_SIM):.5f}')

print('b)')
integral_I, n_I, Scuad_I = estimarIntegral(d, g_I)
print((
    'Valor estimado de la integral, frenando cuando la desviacion estandar muestral del estimador'
    f' es menor que {d} (S={sqrt(Scuad_I):.3f}) ({n_I} iteraciones) {integral_I:.5f}'
))


# ii)
print('ii)')

# La integral de -inf a inf de una funcion par es igual
# a dos veces la integral de la funcion de 0 a inf
def g_II(x):
    return 2 * (x**2) * (exp(- x**2))

print('a)')

# Metodo de Monte Carlo (intervalo (0,inf)) con N simulaciones
def MonteCarlo0INF(g, N):
    integral = 0
    for _ in range(N):
        X = random()
        integral += g(1/X - 1) / (X**2)
    return integral / N

print(f'Valor estimado usando Monte Carlo usual ({N_SIM} simulaciones): {MonteCarlo0INF(g_II, N_SIM):.5f}')

print('b)')
integral_II, n_II, Scuad_II = estimarIntegral(d, lambda x : g_II(1/x - 1) / (x**2))
print((
    'Valor estimado de la integral, frenando cuando la desviacion estandar muestral del estimador'
    f' es menor que {d} (S={sqrt(Scuad_II):.3f}) ({n_II} iteraciones) {integral_II:.5f}'
))
