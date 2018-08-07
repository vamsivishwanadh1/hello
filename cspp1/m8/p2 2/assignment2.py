'''This function takes in one number and returns one number.'''
def sumofdigits(n_in):
    '''
    n is positive Integer

    returns: a positive integer, the sum of digits of n.
    '''
    if n_in == 0:
        return 0
    return n_in%10 + sumofdigits(n_in//10)
def main():
    '''main function'''
    a_in = input()
    print(sumofdigits(int(a_in)))
if __name__ == "__main__":
    main()
