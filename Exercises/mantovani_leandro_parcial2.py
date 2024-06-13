from random import random
import math


# Ejercicio 1

# Funcion de probabilidad de masa de X
# fpmX = [0.13, 0.22, 0.35, 0.3]

def algo_x(p):
    while True:
        Y = int(random() * 4)
        U = random()
        if U < p[Y] / (1.4 * 0.25):
            return Y


# Ejercicio 2

# Funcion para generar X usando transformada inversa
def generarX_ej2():
    U = random()
    if U < 2/3:
        return (3*U/2) ** (2/3)
    else:
        return 3*U - 1


def ejercicio2():
    print('Ejercicio 2)')
    # Estimamos P(X > 4) usando 10_000 simulaciones
    N_SIM = 10_000

    count = 0
    for _ in range(N_SIM):
        X = generarX_ej2()
        if X > 1:
            count += 1

    print((
        f'Valor estimado ({N_SIM} simulaciones) '
        f'de P(X > 1) = {count / N_SIM}'
    ))


# Ejercicio 3

# Funcion lambda(t)
def lamb_fun_ej3(t):
    if t < 0 or t > 9:
        return 0
    elif 0 <= t < 3:
        return 5 + 5 * t
    elif 3 <= t <= 5:
        return 20
    else:
        return 30 - 2 * t


def hot_dog(T):
    # Arreglo de intervalos
    I_arr = [1, 2, 6, 8, 9]
    # Arreglo de lambdas en cada intervalo
    lamb_arr = [10, 15, 20, 18, 14]

    NT, Eventos = 0, []

    # Indice que indica el intervalo actual
    j = 0

    # Genero primer tiempo de arribo con una exp(lamb_j0)
    t = - math.log(1 - random()) / lamb_arr[j]

    while t <= T:
        # Vemos si el tiempo generado cae dentro del intervalo actual
        if t <= I_arr[j]:
            V = random()
            # Veo si rechazo o no el t generado
            if V < lamb_fun_ej3(t) / lamb_arr[j]:
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


def ejercicio3():
    print('Ejercicio 3)')

    # Estimamos el numero esperado de arribos en [0, 9]
    # Usamos 10_000 simulaciones
    N_SIM = 10_000

    eventos = 0
    for _ in range(N_SIM):
        NT, _ = hot_dog(9)
        eventos += NT
    
    print((
        f'El numero estimado ({N_SIM} simulaciones) '
        f'de arribos en [0,9] es: {eventos / N_SIM}'
    ))


# Ejercicio 4

def I(x, y):
    u = abs(x) ** (3/2)
    v = (y - u) ** 2
    return (x ** 2) + v <= 1


def area(N):
    integral = 0
    for _ in range(N):
        X = random()
        Y = random()
        integral += I(-1.5 + 3*X, -1.5 + 3*Y)
    return integral / N


def ejercicio4():
    print('Ejercicio 4)')

    N_SIM = 100_000
    print(f'Area estimada ({N_SIM} simulaciones): {(area(N_SIM)):.6f}')
