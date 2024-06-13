import numpy as np
from math import comb, sqrt
from random import random


# Ejercicio 2
def ejercicio2():
    print('Ejercicio 2:')

    # Cantidad de valores en la muestra observada
    n = 9
    # Estadistico de la muestra observada
    d_obs = 0.153472
    # Numero de simulaciones
    N_SIM = 10_000

    pvalor_ej2 = 0
    for _ in range(N_SIM):
        # Generamos muestra ordenada de n uniformes
        datos = np.random.uniform(0, 1, n)
        datos.sort()

        # Calculamos el estadistico para cada dato
        # de la muestra generada
        d_j = 0
        for j in range(n):
            u_j = datos[j]
            d_j = max(d_j, (j+1)/n - u_j, u_j - j/n)
        
        # Contamos si el estadistico de los datos generados
        # supera el estadistico de la muestra observada
        if d_j >= d_obs:
            pvalor_ej2 += 1

    pvalor_ej2 = pvalor_ej2 / N_SIM
    print(f'd) p-valor: {pvalor_ej2}')


# Ejercicio 3
def ejercicio3():
    print('Ejercicio 3:')

    # Funcion probabilidad de masa de una Bin(n, p)
    def bin_fpm(n, p, i):
        return comb(n, i) * (p ** i) * ((1-p) ** (n-i))

    # Funcion para estimar el parametro p de una
    # variable aleatoria binomial Bin(n, p), con
    # n dado, a partir de un arreglo de frecuencias
    # observadas NF
    def estimar_p_bin(NF, n):
        p = 0
        for i in range(len(NF)):
            p += NF[i] * i
        return p / (sum(NF) * n)

    # Cantidad de valores en la muestra
    N = 1000
    # Valor estimado de p
    p = 0.217
    # Estadistico T de la muestra observada
    t_obs = 3.018119
    # Arreglo de frecuencias en cada iteracion
    NF_j = np.zeros(4, int)
    # Numero de simulaciones
    N_SIM = 10_000

    pvalor_ej3 = 0
    for _ in range(N_SIM):
        # Generamos una muestra de N datos con
        # distribucion Bin(3, p)
        datos = np.random.binomial(3, p, N)
        # Generamos el arreglo de frecuencias
        NF_j *= 0
        for dato in datos:
            NF_j[dato] += 1
        # Estimamos p con la nueva muestra
        p_j = estimar_p_bin(NF_j, 3)
        # Calculamos el estadistico T para la nueva muestra
        t_j = 0
        for i in range(4):
            p_i = bin_fpm(3, p_j, i)
            t_j += ((NF_j[i] - N*p_i) ** 2) / (N*p_i)
        
        # Contamos si el estadistico de los datos generados
        # supera el estadistico de la muestra observada
        if t_j >= t_obs:
            pvalor_ej3 += 1
        
    pvalor_ej3 = pvalor_ej3 / N_SIM
    print(f'd) p-valor: {pvalor_ej3}')


# Ejercicio 4
def ejercicio4():
    print('Ejercicio 4:')

    # Funcion para determinar la media con un intervalo de confianza
    # de 1-alpha, con un ancho menor a L
    def mediaIC(simulacion, z_alpha_2, L):
        # Para el item b), imprimimos la media en las siguientes
        # iteraciones
        NS = [1000, 5000, 7000]

        d = L / (2 * z_alpha_2)
        Media = simulacion(random())  # X(1)
        Scuad, n = 0, 1  # Scuad = S^2(1)
        while n <= 100 or sqrt(Scuad/n) > d:
            n += 1
            # Simulamos Monte Carlo, con una uniforme
            X = simulacion(random())
            MediaAnt = Media
            Media = MediaAnt + (X - Media) / n
            Scuad = Scuad * (1 - 1/(n-1)) + n * (Media-MediaAnt) ** 2

            if n in NS:
                print(f'Iteracion {n}:')
                print(f'   Integral estimada: {Media:.4f}')
                print(f'   S = {sqrt(Scuad):.4f}')
                # El extremo superior del intervalo de confianza es
                IC_max = Media + z_alpha_2 * sqrt(Scuad/n)
                IC_min = Media - z_alpha_2 * sqrt(Scuad/n)
                print(f'   IC: ({IC_min:.4f}, {IC_max:.4f})')
        # Para el ejercicio b, tambien devolvemos la cantidad
        # de iteraciones
        return Media, n
    
    def g(x):
        return x / (1 + x ** 4)
    
    # Funcion para adaptar la g al intervalo
    # (0, 1) y aplicar Monte Carlo
    def monteCarlo0INF(x):
        return g((1/x) - 1) / (x ** 2)
    
    integral, n = mediaIC(monteCarlo0INF, 1.96, 0.002)
    print(f'a) Integral estimada (N_s = {n} iteraciones): {integral:.4f}')
