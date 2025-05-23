SIMULATION_MAX_LIMIT = 10_000

# Estimated probability and estimated number of times to get something
# done until success with probability p (Geometric distribution mean). 
# The simulation and its arguments are given by func and args.
# Note that it is required that the simulation returns 1 if the value
# satisfies the probability condition and 0 otherwise.
def sim_statistics(func, args, N):
    acc_prob, acc_mean = 0, 0
    for _ in range(N):
        X = func(*args)
        
        # Probability accumulator
        acc_prob += X

        # Mean accumulator
        tries = 1
        while (X == 0 and tries < SIMULATION_MAX_LIMIT):
            tries += 1
            X = func(*args)
        
        if tries < SIMULATION_MAX_LIMIT:
            acc_mean += tries

    return acc_prob / N, acc_mean / N
