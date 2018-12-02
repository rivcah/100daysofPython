mydict = {
    1 : 'Hannah',
    2 : 'Ava',
    3 : 'Katie',
    4 : 'Holly'
    }

ascending = sorted(mydict.items(), key = lambda x: x[1])
descending = sorted(mydict.items(), key = lambda x: x[1], reverse = True)

print("The list in ascending order:\n")

for key, value in ascending:
    print("{} : {}".format(key, value))

print("\nThe descending list is:\n")

for key, value in descending:
    print("{} : {}".format(key, value))
    
