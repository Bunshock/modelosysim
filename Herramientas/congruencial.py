import argparse


# Non-negative integer type definition for argument parser
def non_negative_int(val):
    i_val = int(val)
    if i_val < 0:
        raise argparse.ArgumentTypeError(
            "%s is an invalid non-negative float value" % val)
    return i_val


# Next number in congruential generator sequence
def congruentialNext(M, a, c, y):
    return (a*y + c) % M


# For a given generator and a starting point, it calculates if
# for some 1 <= K < M, yK = start
# Returns 1 <= K < M if period was found, or 0 if not
def sequencePeriodFrom(M, a, c, start):

    u, period = congruentialNext(M, a, c, start), 0

    while (period < M and u != start):
        u = congruentialNext(M, a, c, u)
        period += 1

    if period >= M:
        period = -1

    return period + 1


# For a given generator, returns the period length
# if a period is found. Returns 0 otherwise
def sequencePeriod(M, a, c, seed):

    period = 0
    start_pos, start_seed = 0, seed

    while start_pos < M and period == 0:
        period = sequencePeriodFrom(M, a, c, start_seed)
        start_seed = congruentialNext(M, a, c, start_seed)
        start_pos += 1

    return period, start_pos - 1


if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    # Congruential sequence parameters
    parser.add_argument('M', type=non_negative_int, help='Modulus')
    parser.add_argument('a', type=int, help='Multiplier')
    parser.add_argument('c', type=int, help='Increment')
    parser.add_argument('seed', type=int, help='Seed')

    # Possible actions
    parser.add_argument(
        '-N',
        type=non_negative_int,
        default=-1,
        help='Print first N sequence values')
    parser.add_argument(
        '-P',
        action='store_true',
        default=False,
        help='Calculate sequence period')
    parser.add_argument(
        '-S',
        action='store_true',
        default=False,
        help='Calculate seeds to maximize sequence period')

    args = parser.parse_args()

    print("------- INPUT PARAMETERS -------")
    print(f'Congruential sequence: '
          'yn+1 = {args.a} * yn + {args.c}   mod {args.M}')
    print(f'Initial value: y0 = {args.seed}')

    # Print first N sequence numbers
    if args.N > 0:
        print(f"------- FIRST {args.N} SEQUENCE NUMBERS -------")
        u = args.seed
        for i in range(args.N):
            print(f'(y{i}: {u})', end=" ")
            u = congruentialNext(args.M, args.a, args.c, u)
        print('')

    # Calculate sequence period (K)
    if args.P:
        print("------- SEQUENCE PERIOD -------")
        period, period_start_pos = sequencePeriod(
            args.M, args.a, args.c, args.seed)
        if period > 0:
            print(f"Sequence period (K): {period}")
            print(f"Starting position: y{period_start_pos}")
        else:
            print("Sequence period wasn't found!")

    if args.S:
        print("------- SEEDS WITH MAXIMUM PERIOD -------")
        # We brute force for every possible seed (values in range 0,...,M-1)
        # Note that we have two cases: For a mixed congruential generator, the
        # period is at most M.
        # For a puerly multiplicative congruential generator (c = 0), the
        # period is at most M-1.
        longest_period, max_seeds = (0, 0, 0), []
        for test_seed in range(args.M):
            period_length, period_start = sequencePeriod(
                args.M, args.a, args.c, test_seed)
            if period_length > 0 and period_length > longest_period[0]:
                longest_period = (period_length, period_start, test_seed)
            if (period_length == args.M and args.c > 0) or \
            (period_length == args.M - 1 and args.c == 0):
                max_seeds.append(test_seed)

        if longest_period[0] > 0 and (
                (longest_period[0] < args.M and args.c > 0) or
                (longest_period[0] < args.M - 1 and args.c == 0)):
            print(f'Maximum period found: {longest_period[0]},  '
                  'for seed: {longest_period[2]},  '
                  'starting at y{longest_period[1]}')
        elif (longest_period[0] == args.M and args.c > 0) or \
        (longest_period[0] == args.M - 1 and args.c == 0):
            print(f"Maximum period found is {longest_period[0]}!!")
            print(f"Seeds for which the generator has maximum period (K=M): ",
                  end='')
            for seed in max_seeds:
                print(seed, end=' ')
            print('')
        else:
            print("This generator has no possible seeds for which K=M  :c")
