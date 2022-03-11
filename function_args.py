def ex_item(*args, key=False):
    new_list =[]
    for i in args:
        for y in i:
            if y not in new_list:
                new_list.append(y)
    if key == True:
        new_list.sort()
    return new_list

z = [3, 7, 5]
x = [4, 5, 3, 2, 1, 8]
c = [4, 5, 3, 8, 9, 3, 3, 6, 5]

t = ex_item(z, x, c, key=True)
