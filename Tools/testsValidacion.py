import numpy as np
# Usamos scipy para pasar las funciones fpm, F y 
# generadores aleatorios de distribuciones
from scipy.stats import binom

# Test de validacion de Pearson para datos discretos
# con parametros especificados. Se supone que en H0
# se propone una distribucion con funcion de probabilidad
# de masa 'fpm', que toma 'k+1' valores 0,1,...,k.
# Tambien se provee una funcion 'simular' para generar
# aleatoriamente un valor con dicha distribucion.
# Se estima el p-valor usando N_SIM simulaciones
# NOTA: Para una distribucion de Poissson, es necesario
# usar una cota para el valor maximo
def testPearsonDiscretos(N_SIM, muestra, k, fpm, simular):
    N = len(muestra)
    # Calculamos las frecuencias observadas en la muestra observada
    NF_obs = np.zeros(k+1, int)
    for observacion in muestra:
        NF_obs[observacion] += 1
    # Primero calculamos el estadistico con la muestra observada
    t_obs = 0
    for i in range(k+1):
        p_i = fpm(i)
        t_obs += ((NF_obs[i] - N*p_i) ** 2) / (N*p_i)

    # Arreglo para datos simulados
    datos = np.zeros(N, int)
    # Arreglo de frecuencias observadas de datos simulados
    NF = np.zeros(k+1, int)
    # Probabilidades esperadas de datos simulados
    p = np.zeros(k+1, int)

    pvalor = 0
    for _ in range(N_SIM):
        # Generamos muestra de datos simulados
        for j in range(N):
            datos[j] = simular()
        NF *= 0
        # Generamos arreglo de frecuencias esperadas
        for dato in datos:
            NF[dato] += 1
        # Calculamos el estadistico T para la muestra simulada
        T = 0
        for i in range(k+1):
            p_i = fpm(i)
            T += ((NF[i] - N*p_i) ** 2) / (N*p_i)
        if T >= t_obs:
            pvalor += 1
    
    return pvalor / N_SIM

# Test de validacion de Pearson para datos discretos
# con m parametros no especificados. 'estimadores'
# contiene las funciones necesarias para estimar cada uno
# de los m parametros
def testPearsonDiscretosEstimando(N_SIM, estimadores, muestra, k, fpm, simular, *parametros):
    N = len(muestra)
    # Calculamos las frecuencias observadas en la muestra observada
    NF_obs = np.zeros(k+1, int)
    for observacion in muestra:
        NF_obs[observacion] += 1
    estimados = []
    
    # Estimamos los parametros no especificados
    for estimador in estimadores:
        estimados.append(estimador(muestra, k, *parametros))
    
    # Calculamos el estadistico con la muestra observada
    t_obs = 0
    for i in range(k+1):
        # A FUTURO: no tendria que haber un orden entre los
        # parametros estimados y especificados
        p_i = fpm(i, *parametros, *estimados)
        t_obs += ((NF_obs[i] - N*p_i) ** 2) / (N*p_i)

    # Arreglo para datos simulados
    datos = np.zeros(N, int)
    # Arreglo de frecuencias observadas de datos simulados
    NF = np.zeros(k+1, int)
    # Probabilidades esperadas de datos simulados
    p = np.zeros(k+1, int)

    pvalor = 0
    for _ in range(N_SIM):
        # Generamos muestra de datos simulados
        for j in range(N):
            datos[j] = simular(*parametros, *estimados)
        NF *= 0
        # Generamos arreglo de frecuencias esperadas
        for dato in datos:
            NF[dato] += 1
        # Estimamos parametros para la nueva muestra
        estimados_j = []
        for estimador in estimadores:
            estimados_j.append(estimador(datos, k, *parametros))
        # Calculamos el estadistico T para la muestra simulada,
        # usando los parametros estimados con esta nueva muestra
        T = 0
        for i in range(k+1):
            p_i = fpm(i, *parametros, *estimados_j)
            T += ((NF[i] - N*p_i) ** 2) / (N*p_i)
        if T >= t_obs:
            pvalor += 1
    
    return pvalor / N_SIM


# Test de Kolmogorov-Smirnov para datos continuos. Se
# supone que en H0 se propuso una distribucion 'F' con
# parametros 'parametros'.
# Se simula el p-valor con 'N_SIM' simulaciones
def testKolmogorovSmirnov(N_SIM, muestra, F):
    N = len(muestra)
    # Ordenamos la muestra de menor a mayor
    muestra.sort()

    # Calculamos el estadistico D para la muestra observada
    d_obs = 0
    for j in range(N):
        Y = muestra[j]
        d_obs = max(d_obs, (j+1)/N - F(Y), F(Y) - j/N)
    
    # Calculamos el p-valor
    pvalor = 0
    for _ in range(N_SIM):
        # Generamos una muestra de N uniformes (ver teorema)
        uniformes = np.random.uniform(0, 1, N)
        uniformes.sort()
        # Calculamos el estadistico D para la nueva muestra
        d_j = 0
        for j in range(N):
            u_j = uniformes[j]
            d_j = max(d_j, (j+1)/N - u_j, u_j - j/N)
        if d_j >= d_obs:
            pvalor += 1
    
    return pvalor / N_SIM


# Test de Kolmogorov-Smirnov para datos continuos, estimando
# m parametros. Las funciones en 'estimadores' estiman cada
# uno de los parametros no especificados. La funcion 'simular'
# genera aleatoriamente un dato con distribucion 'F'.
def testKolmogorovSmirnovEstimando(N_SIM, estimadores, muestra, F, simular, *parametros):
    N = len(muestra)
    # Ordenamos la muestra de menor a mayor
    muestra.sort()

    # Estimamos los parametros no especificados
    estimados = []
    for estimador in estimadores:
        estimados.append(estimador(muestra, *parametros))
    
    # Calculamos el estadistico D para la muestra observada
    d_obs = 0
    for j in range(N):
        Y = muestra[j]
        F_j = F(Y, *parametros, *estimados)
        d_obs = max(d_obs, (j+1)/N - F_j, F_j - j/N)
    
    # Calculamos el p-valor
    pvalor = 0
    for _ in range(N_SIM):
        datos = []
        for _ in range(N):
            datos.append(simular(*parametros, *estimados))
        datos.sort()
        # Estimamos los parametros con la nueva muestra
        estimados_j = []
        for estimador in estimadores:
            estimados_j.append(estimador(muestra, *parametros))
        # Calculamos el estadistico D para la nueva muestra
        d_j = 0
        for j in range(N):
            Y = datos[j]
            F_j = F(Y, *parametros, * estimados_j)
            d_j = max(d_j, (j+1)/N - F_j, F_j - j/N)
        if d_j >= d_obs:
            pvalor += 1
    
    return pvalor / N_SIM


# NOTAR: puedo generalizar las versiones con parametros sin especificar
# juntando con la otra version

def F(x):
    return 1 - np.e ** (-(1/50.0)*x)
muestra = [86.0, 133.0, 75.0, 22.0, 11.0, 144.0, 78.0, 122.0, 8.0, 146.0, 33.0, 41.0, 99.0]
pvalor = testKolmogorovSmirnov(1_000, muestra, F)

print(f'pvalor kolmogorov: {pvalor}')
