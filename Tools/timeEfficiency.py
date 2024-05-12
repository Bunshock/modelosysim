# Time efficiency calculator decorator
from time import time

def timeEfficiency(fun, *args):
    def wrapper():
        start_time = time()
        result = fun(*args)
        end_time = time()
        return result, end_time - start_time
    return wrapper()
