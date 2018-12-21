def ref_search(in_list, x):
    if len(in_list) < 1 :
        return -1
    if x < in_list[0] or x > in_list[-1]:
        return -1
    if len(in_list)==1:
        return 0
    n = len(in_list)//2
    indx1 = 0
    indx2 = len(in_list)
    d = (indx2-indx1)//2

    while d >= 1:

        if x == in_list[n]:
            return n
        elif x > in_list[n]:
            indx1 = n
            n = n + d
        else:
            indx2 = n
            n = n - d
        d = (indx2-indx1)//2



print ref_search([22, 23],22)
def my_search(in_list, x):
    return -1
