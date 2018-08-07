''' Exercise: Assignment-1'''
def factorial(n_in):
    '''
    n is positive Integer

    returns: a positive integer, the factorial of n.
    '''
    if n_in in (0, 1):
        return 1
    return n_in*factorial(n_in-1)
def main():
    '''main function'''
    a_in = input()
    print(factorial(int(a_in)))
if __name__ == "__main__":
    main()
