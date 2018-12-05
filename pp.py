##Using class and functions to generate and ID number for a name.

class people:

      
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

    def getlist(path):
        
        import csv

        with open(path, "w+") as file:
            f = csv.writer(file)
            f.writerow(("Name", "ID"))
            f.writerow((people.getname(), people.getid()))
            file.close()
            
        
    
    


    
        
        

    
