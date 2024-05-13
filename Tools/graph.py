import matplotlib.pyplot as plt
from collections import Counter


# Graph discrete distribution given an array of numbers 'x_vec' generated
# by said distribution with 'N_SIM' iterations
def graphDVA(x_vec, N_SIM, title='Graph'):

    # Get probabilities array
    x_vec_counts = Counter(x_vec)
    probs_vec = [count/N_SIM for count in x_vec_counts.values()]

    x_axis_vec = x_vec_counts.keys()
    x_min, x_max = min(x_vec_counts.keys()), max(x_vec_counts.keys())
    
    # Set up graph title and axis lines
    plt.title(f'{title}\nSimulations: {N_SIM}')
    plt.grid(axis='y', color='blue', linestyle='--', linewidth=0.5)

    # Graph histogram
    plt.bar(x=x_axis_vec, height=probs_vec, width=1, color = 'lightblue', edgecolor = 'black')
    plt.xticks(range(x_min, x_max + 1))
    plt.xlim([x_min - 1, x_max + 1])

    # Show graph
    plt.show()


# Graph continuous distribution given an array of dots 'dots_vec' generated
# by said distribution with 'N_SIM' iterations
def graphCVA(x_vec, y_vec, N_SIM, title='Graph'):
    
    # Set up graph title and axis lines
    plt.title(f'{title}\nSimulations: {N_SIM}')
    plt.grid(axis='y', color='orange', linestyle='--', linewidth=0.5)

    # Scatter dots on grid
    plt.scatter(x=x_vec, y=y_vec, color='red', s=1)

    # Show graph
    plt.show()
