def count_list(par, par_2 = False,  count = 0):
    if par_2 == True:
        typ = type(par[0])
        for i in par:
            count += 1
        return count, typ
    else:
        for i in par:
            count +=1
        return count


j = [9,8,7,6]

count_list(j, True)

