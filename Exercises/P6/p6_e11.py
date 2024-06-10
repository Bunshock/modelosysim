from scipy.stats import binom


# Muestra observada
muestra = [6, 7, 3, 4, 7, 3, 7, 2, 6, 3, 7, 8, 2, 1, 3, 5, 8, 7]
print(f'Muestra observada: {muestra}')

hipotesis = 'H0) Los datos provienen de una binomial Bin(n=8, p)'
print(hipotesis)

# Estimador de parametro p de una binomial Bin(n, p) a
# partir de una muestra. n >= max(muestra)
def estimadorPBinomial(n, muestra):
    return sum(muestra) / (len(muestra) * n)


# Estimador T a partir de las frecuencias de una muestra
# (NF) y considerando una distribucion Bin(n, p)
def estadisticoTBinomial(n, p, NF):
    T = 0
    # Cantidad de valores observados
    N = sum(NF)
    # Creamos el elemento de distribucion binomial
    distBin = binom(n, p)
    # Calculamos el estadistico
    for i in range(len(NF)):
        p_i = distBin.pmf(i)
        T += ((NF[i] - N*p_i) ** 2) / (N*p_i)
    return T


# Valor maximo para la binomial
n = 8
# Frecuencias observadas
NF = [muestra.count(i) for i in range(n+1)]
# Cantidad de observaciones
N = len(muestra)
# Estimacion de p usando la muestra
p_estimado = estimadorPBinomial(n, muestra)
print(f'p_estimado = {p_estimado}')
# Estadistico t_observado
t_observado = estadisticoTBinomial(n, p_estimado, NF)
print(f't_observado = {t_observado}')

# Elemento de distribucion binomial
distBin = binom(n, p_estimado)

# Calculamos el p-valor con N_SIM simulaciones
pvalor = 0
N_SIM = 1_000
for _ in range(N_SIM):
    # Generamos una muestra de N valores de Bin(8, p_estimado)
    muestra_j = []
    for _ in range(N):
        muestra_j.append(distBin.rvs())
    # Calculamos las frecuencias observadas de esta muestra
    NF_j = [muestra_j.count(i) for i in range(n+1)]
    # Estimamos el valor de p para esta muestra
    p_j = estimadorPBinomial(n, muestra_j)
    # Calculamos el estadistico t_j para esta muestra con el
    # nuevo valor estimado de p
    t_j = estadisticoTBinomial(n, p_j, NF_j)
    # Contamos el estadistico
    if t_j >= t_observado:
        pvalor += 1

# Calculamos el p-valor
pValor = pvalor / N_SIM
print(f'p-valor = {pValor}')

# Verificamos el nivel de rechazo
rechazo = float(input('Inserte el porcentaje (nivel) de rechazo (valor entre 0 y 100): ')) / 100.0
if pValor < rechazo:
    print('Hipotesis H0 rechazada')
else:
    print((
        'Hipotesis H0 no rechazada:'
        f'  Los valores podrian provenir de una Bin(8, {p_estimado:.4f})'
    ))
