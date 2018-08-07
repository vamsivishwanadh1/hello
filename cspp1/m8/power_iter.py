# Exercise: PowerIter
# Write a Python function, iterPower(base, exp), that takes in two numbers and returns the base^(exp) of given base and exp.

# This function takes in two numbers and returns one number.


def iterPower(base, exp):
    i = 1
    if base == 1:
        return 1
    else:
        result = 1
        while i <= exp:
            result *= base
            exp = exp - 1
    return result
    
def main():
    "'prints power of a given number'"
    data = input()
    data = data.split()
    print(iterPower(float(data[0]),int(data[1])))
if __name__== "__main__":
        main()
    
