##Function that evaluates three numbers and returns the largest one.
##There's another fucntion which is used to test some values and check if
##the function max_num works.
def max_num(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return(num1)
    elif num2 > num1 and num2 > num3:
        return(num2)
    elif num3 > num1 and num3 > num2:
        return(num3)
    else:
        return("It's a tie!")



def try_func():
    print(max_num(-10, 0, 10))
    print(max_num(-10, 5, -30))
    print(max_num(-5, -10, -10))
    print(max_num(2, 3, 3))
    
