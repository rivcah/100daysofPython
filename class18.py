def getclass18():

    names = input("Enter the name of students in the Class of '18, separated by space:\n").split(' ')
    grades = input("Enter their grades, also separated by spaces:\n").split(' ')
    return(names, grades)

def getcsv(path):

    import csv
    
    names, grades = getclass18()
    class18 = dict(zip(names, grades))

    with open(path, 'w+') as file:
        f = csv.writer(file)
        for key, value in class18.items():
            f.writerow([key, value])
        file.close()


def getchanges(path):

    import csv

    with open(path, 'r') as file:
        r = csv.reader(file)
        class18 = dict(r)

    return(class18)

        



