def append_sum(lst):
    n = 0

    while n < 3:
        lst.append(sum(lst[-2:]))
        n+=1

    return(lst)
