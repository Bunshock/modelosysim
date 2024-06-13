from math import sqrt

# Estimador de la media con N_SIM simulaciones
def mediaNSIM(simulacion, N_SIM):
    media = 0
    for _ in range(N_SIM):
        X = simulacion()
        media += X
    return media / N_SIM


# Estimador de la media con ECM < d
def mediaECM(simulacion, d):
    Media = simulacion()  # X(1)
    Scuad, n = 0, 1  # Scuad = S^2(1)
    while n <= 100 or sqrt(Scuad/n) > d:
        n += 1
        X = simulacion()
        MediaAnt = Media
        Media = MediaAnt + (X - Media) / n
        Scuad = Scuad * (1 - 1/(n-1)) + n * (Media-MediaAnt) ** 2
    return Media


# Estimador de la media usando intervalo de confianza
# de alph% (proporcionando el valor de z_alph/2), con 
# un ancho menor a L
def mediaIC(simulacion, z_alph_2, L):
    return mediaECM(simulacion, L / (2 * z_alph_2))


# Estimador de proporcion usando ECM < d
def proporcionECM(simulacion, d):
    p, n = 0, 0
    # Para X ~ Bernoulli: Var(X) = p(1-p)
    while n <= 100 or sqrt(p * (1-p)/n) > d:
        n += 1
        X = simulacion()
        p = p + (X - p) / n
    return p


# Estimador de proporcion usando intervalo de confianza
# de alph% (proporcionando el valor de z_alph/2), con 
# un ancho menor a L
def proporcionIC(simulacion, z_alph_2, L):
    return proporcionECM(simulacion, L / (2 * z_alph_2))
