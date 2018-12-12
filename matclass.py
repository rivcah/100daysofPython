class matrix:

    def greeting():
        greeting = "Hello there! This program generates a square matrix with random numbers from 1 to 100. You can choose the size of your matrix and decide to save it as a .csv file. Try it now! Have fun!\n\n\n\n"
        print(greeting)

    def intro():
        matrix.greeting()
        n = int(input("Enter the size of the matrix you want to create:\n"))
                
        return(n)



    def getmatrix():
        import random as r

        newlist = []

        n = matrix.intro()
        m = n**2

        for i in range(n):
            newlist.append(list())

        j = 0
        k = 0

        while j < n:
            for k in range(n):
                newlist[k].append(str(r.randint(1, 101)))
            j += 1

        print("A "+str(n)+" by "+str(n)+" matrix will be created a total of "+str(m)+" random numbers will be generated.")

        return(newlist)

    def getdata():

        filename = input("Enter the name of the file:\n")
        path = '/home/rivcah/Documents/PythonFiles/'
        extension = '.csv'

        return(path+filename+extension)


    def process():
        import csv

        newlist = matrix.getmatrix()
        fn = matrix.getdata()
 
                
        with open(fn, 'w+') as file:
            f = csv.writer(file)
            for t in range(len(newlist)):
                f.writerow(newlist[t])
            file.close()



        
        

        
        

    


    


    
