p = input('Choose chapter: ')
ex = input('Choose exercise: ')

X = __import__(f'Exercises.P{p}.p{p}_e{ex}')
