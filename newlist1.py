##This program finds all the numbers between 1500 and 2700 that are
##divisible by 5 and 7.

n = range(1500, 2700)
newlist = []

for i in n:
    if (i%7==0) and (i%5==0):
        newlist.append(str(i))

print(newlist)
