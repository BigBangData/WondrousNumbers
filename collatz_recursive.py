import sys
from collections.abc import Iterable

def check_args():
    """Check user input for arguments and correctness of arguments.
    """
    err_msg = 'ERROR: Must provide a single natural number.\nUSAGE:\
 $ python wondrous.py <positive_integer>'
    # check if an arg was passed
    if len(sys.argv) != 2:
        print(err_msg); sys.exit(1)
    else:
        # check that arg can be converted to int
        try:
            arg = int(sys.argv[1])
        except ValueError as e1:
            print(''.join(['ERROR: ', str(e1)]))
            sys.exit(1)
        # check that it is a natural number
        if arg <= 0:
            print(err_msg); sys.exit(1)
        else:
            return arg

def flatten_list(x):
    if isinstance(x, Iterable):
        return [a for b in x for a in flatten_list(b)]
    else:
        return [x]

def wondrous_numbers(n, m=None):
    """Given a scalar argument x, return a list with the hailstone
    sequence of wondrous numbers for x and the number of operations
    that took to get to 1. 
    
    Assume all natural numbers are wondrous,
    that is, that the Collatz conjecture is true and they all 
    converge to 1.
    """
    if n == 1:
        if isinstance(m, Iterable):
            return m[1:], len(m)-1
        else:
            return [m], len(m)
    else:
        if n % 2 == 0:
            n = int(n/2)
        else:
            n = n*3 +1 
        m = flatten_list([m, n])
        return wondrous_numbers(n, m)


if __name__=='__main__':
    x = check_args()
    seq, num = wondrous_numbers(x)
    print(f'Hailstone seq: {seq}')
    print(f'Number of ops: {num}')