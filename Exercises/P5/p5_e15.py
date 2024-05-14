from random import random
import math


# a) Algoritmo de generacion de proceso Poisson no homogeneo
# con adelgazamiento
def Poisson_no_homogeneo_adelgazamiento(lamb_fun, lamb, T, t0=0):
    NT, Eventos = 0, []
    U = 1 - random()

    # Simulamos primer tiempo de arribo
    t = - math.log(U) / lamb + t0

    while t <= T:
        # Vemos si aceptamos o no el evento
        V = random()
        if V < lamb_fun(t) / lamb:
            NT += 1
            Eventos.append(t)
        # Simulamos el proximo tiempo de arribo
        t += - math.log(1 - random()) / lamb
    
    return NT, Eventos


# Simulamos los procesos con 10_000 iteraciones
print('a)')
N_SIM = 10_000

# (i) Elijo lambda = 7, calculamos P(N(2) <= 9)
print('(i)')

def lambda_I(t):
    return (0 <= t <= 3) * (3 + 4 / (t+1))

count_I = 0
for _ in range(N_SIM):
    NT_I, _ = Poisson_no_homogeneo_adelgazamiento(lambda_I, 7, 2)
    if NT_I <= 9:
        count_I += 1

count_I_b = 0
for _ in range(N_SIM):
    NT_I_b, _ = Poisson_no_homogeneo_adelgazamiento(lambda_I, 13/3, 2.9, t0=2.5)
    if NT_I_b <= 2:
        count_I_b += 1

print(f'Valor exacto de P(N(2) <= 9) = 0.409656')
print(f'Valor estimado ({N_SIM} simulaciones) de P(N(2) <= 9) = {(count_I / N_SIM):.5f}')
print(f'Valor exacto de P(N(2.9) - N(2.5) <= 2) = 0.774835')
print(f'Valor estimado ({N_SIM} simulaciones) de P(N(2.9) - N(2.5) <= 2) = {(count_I_b / N_SIM):.5f}')

# (ii) Elijo lambda = 21, calculamos P(N(2) <= 30)
print('(ii)')

def lambda_II(t):
    if t < 0 or t > 5: return 0
    else: return (t-2)**2 - 5*t + 17

count_II = 0
for _ in range(N_SIM):
    NT_I, _ = Poisson_no_homogeneo_adelgazamiento(lambda_II, 21, 2)
    if NT_I <= 30:
        count_II += 1

print(f'Valor exacto de P(N(2) <= 30) = 0.775532')
print(f'Valor estimado ({N_SIM} simulaciones) de P(N(2) <= 30) = {(count_II / N_SIM):.5f}')

# (iii) Elijo lambda = 0.5, calculamos P(N(5) > 1)
print('(iii)')

def lambda_III(t):
    if t < 2 or t > 6: return 0
    elif 2 <= t <= 3: return (t / 2) - 1
    else: return 1 - (t / 6)

count_III = 0
for _ in range(N_SIM):
    NT_I, Eventos = Poisson_no_homogeneo_adelgazamiento(lambda_III, 0.5, 5)
    if NT_I > 1:
        count_III += 1

print(f'Valor exacto de P(N(5) > 1) = 0.233622')
print(f'Valor estimado ({N_SIM} simulaciones) de P(N(5) > 1) = {(count_III / N_SIM):.5f}')


# b) Mejorar el algoritmo anterior usando al menos 3 intervalos
print('b)')

# Mejora del algoritmo de adelgazamiento
# lamb_arr: arreglo con el lambda designado para cada intervalo
# I_arr: arreglo con limites derechos de cada intervalo
def Poisson_adelgazamiento_mejorado(lamb_fun, lamb_arr, I_arr, T, t0=0):
    NT, Eventos = 0, []

    # Indice que indica el intervalo actual
    j = 0
    # Movemos j dependiendo del tiempo inicial t0
    while j >= I_arr[j]: j+= 1

    # Genero primer tiempo de arribo con una exp(lamb_j0)
    t = - math.log(1 - random()) / lamb_arr[j] + t0

    while t <= T:
        # Vemos si el tiempo generado cae dentro del intervalo actual
        if t <= I_arr[j]:
            V = random()
            # Veo si rechazo o no el t generado
            if V < lamb_fun(t) / lamb_arr[j]:
                NT += 1
                Eventos.append(t)
            t += - math.log(1 - random()) / lamb_arr[j]
        else: # t > I_arr[j]
            # Si el tiempo generado cae fuera del intervalo actual,
            # lo transformo como si hubiera sido generado por la exponencial
            # exp(lamb_j+1), y cambio el indice que indica el intervalo actual
            t = I_arr[j] + (t - I_arr[j]) * lamb_arr[j] / lamb_arr[j+1]
            j += 1
    
    return NT, Eventos

# Ejemplo de uso: tomo el ejercicio (iii) con estos parametros:
# Intervalos: [3, 4, 5, 6]
# Lambdas: [0.5, 0.5, 1/3, 1/6]
# Calculamos nuevamente P(N(5) > 1)

I_arr = [3, 4, 5, 6]
lamb_arr = [0.5, 0.5, 1/3, 1/6]

count_mejoraIII = 0
for _ in range(N_SIM):
    NT, _ = Poisson_adelgazamiento_mejorado(lambda_III, lamb_arr, I_arr, 5)
    if NT > 1:
        count_mejoraIII += 1

print(f'Valor exacto de P(N(5) > 1) = 0.233622')
print(f'Valor estimado con mejora ({N_SIM} simulaciones) de P(N(5) > 1) = {(count_mejoraIII / N_SIM):.5f}')
