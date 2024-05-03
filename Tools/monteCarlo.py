from random import random
import matplotlib.pyplot as plt
import math
import numpy as np

# Maybe change to Hash-map
MONTE_CARLO_METHOD = {
    '1-01': lambda g, x: g(x),
    '1-AB': lambda g, a, b, x: g(a + (b-a) * x),
    '1-0INF': lambda g, x: g((1/x) - 1) / (x ** 2),
    '2-01': lambda g, x, y: g(x, y),
    '2-AB': lambda g, a, b, c, d, x, y: g(a + (b-a)*x, c + (d-c)*y),
    '2-0INF': lambda g, x, y: g(1/x - 1, 1/y - 1) / ((x ** 2) * (y ** 2))
}


# Returns the aproximated value of the area under the curve on the
# specified interval, depending on the number of iterations N
# If graph is set to True, it shows a graph of the calculation
# (with values adapted to the (0, 1) interval)
# For now, it only works with a single variable calculation
def monteCarlo(method, *args, N, graph=False):
    if graph:
        x_vec, y_vec = [], []
    
    integral = 0
    for _ in range(N):
        X = random()
        y = MONTE_CARLO_METHOD[method](*args, X)

        if graph:
            x_vec.append(X)
            y_vec.append(y)

        integral += y

    if graph:
        # Show every calculated point in a graph
        plt.scatter(x_vec, y_vec)

        # Set x and y axis
        plt.xticks(range(math.floor(min(x_vec)), math.ceil(max(x_vec))+1))

        y_step = max(y_vec) / 15
        plt.yticks(np.arange(min(y_vec), max(y_vec)+y_step, y_step))
        
        # Draw lines between x axis and graph points
        plt.vlines(x_vec, 0, y_vec)
        
        # Show horizontal grid lines
        plt.grid(axis='y')

        # Show the graph
        plt.show()

    return integral / N
