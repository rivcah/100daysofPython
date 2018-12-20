def plotit(path):
    import matplotlib.pyplot as pplt

    w = list(range(1, 9))
    sbd = [0, 6, 11, 12, 9, 8, 13, 12]
    sjd = [8, 9, 7, 9, 15, 12, 5, 6]
    ext = '.png'
    fn = path+ext

    fig = pplt.figure()

    pplt.plot(w, sbd, 'k*', label = 'St. Brides')
    pplt.plot(w, sjd, 'r*', label = 'St. James')

    pplt.xlim(0, 9)
    pplt.ylim(0, 18)
    pplt.xlabel("Number of weeks from December 1664 to February 1665")
    pplt.ylabel("Number of deaths by Parish")

    pplt.title("Accounts of plague death in the year 1665 \n According to the Daniel Defoe's book")

    pplt.legend()

    pplt.show()

    fig.savefig(fn, bbox_inches = 'tight')

