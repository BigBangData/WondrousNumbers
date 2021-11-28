import sys

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

def wondrous_numbers(x):
    """Given a scalar argument x, return a list with the hailstone
    sequence of wondrous numbers for x and the number of operations
    that took to get to 1. 
    
    Assume all natural numbers are wondrous,
    that is, that the Collatz conjecture is true and they all 
    converge to 1.
    """
    seq = []
    while x > 1:
        if x % 2 == 0:
            x = x/2
        else:
            x = x*3 +1
        seq.append(int(x))
    return seq


if __name__=='__main__':
    x = check_args()
    seq = wondrous_numbers(x)
    print(f'Hailstone seq: {seq}')
    print(f'Number of ops: {len(seq)}')