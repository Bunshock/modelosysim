pract = input('Seleccionar practico: ')
ex = input('Seleccionar ejercicio: ')

X = __import__(f'EjerciciosResueltos.Practico{pract}.p{pract}_e{ex}')
