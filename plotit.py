def plotit(path):
    import matplotlib.pyplot as pplt

    fn = path+'.png'

    stmt = list(input("Enter the data for axis x, separated by space:\n").split(' '))
    stmt1 = list(input("Enter the data for axis y, separated by space:\n").split(' '))

    xcoord = list()
    ycoord = list()

    for i in range(len(stmt)):
        xcoord.append(int(stmt[i]))

    for i in range(len(stmt1)):
        ycoord.append(int(stmt1[i]))

    xl = ''
    yl = ''
    tt = 'My Plot'


    c1 = input("Do you want to add labels? Y/N or y/n \n")
    c2 = input("Do you want to add a title to the graph? Y/N or y/n\n")

    if c1 == 'Y' or c1 == 'y':
        xl = input("Type the x label:\n")
        yl = input("Type the y label:\n")


    if c2 == 'Y' or c2 == 'y':
        tt = input("Type the title:\n")
    else:
        print("A standard title will be added")

    xmin = min(xcoord)-5
    xmax = max(xcoord)+5
    ymin = min(ycoord)-5
    ymax = max(ycoord)+5
    

    fig = pplt.figure()
    pplt.plot(xcoord, ycoord, 'r*')
    pplt.xlabel(xl)
    pplt.ylabel(yl)
    pplt.title(tt)
    pplt.xlim(xmin, xmax)
    pplt.ylim(ymin, ymax)
    pplt.show()

    fig.savefig(fn, bbox_inches = 'tight')
    

    






            
