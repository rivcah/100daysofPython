def lottery(num):
    x = int(input("Enter a number from 1 to 500:\n"))
    if x == num:
        print("You won!")
    else:
        print("Oh no! You lost!")


def guess():
    import random as r
    num = r.randint(1, 501)
    lottery(num)
    

    
