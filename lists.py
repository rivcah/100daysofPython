##Use lista.getlist(t, path) in order to create a .csv file with names and
##ID numbers.

class lista:

    def getid():
        import random as r
        
        n = []
        for i in range(5):
            n.append(str(r.randint(0,9)))

        ID = ''
        for i in range(len(n)):
            ID += n[i]

        return(ID)


    def getname():
        
        first = input("First name: ")
        last = input("Last name: ")
        name = first+' '+last

        return(name)


    def register(t):

        i = 1

        names = []
        identity = []

        while i <= t:
            names.append(lista.getname())
            identity.append(lista.getid())
            i += 1

        return(names, identity)


    def getlist(t, path):

        import csv

        names, identity = lista.register(t)
        rows = zip(names, identity)

        with open(path, 'w+') as file:
            f = csv.writer(file)
            f.writerow(("Name", "ID"))
            for row in rows:
                f.writerow(row)
            file.close()

            
        
        
    
        
    
