##Returns the mazimum of three numbers.

def max_of_two(a, b):
    if a > b:
        return(a)
    else:
        return(b)

def maxnum(a, b, c):
    return(max_of_two(a, max_of_two(b, c)))
