def ref_search(in_list, x):
    for i in range(0, len(in_list)):
        if in_list[i]==x:
            return i
    return  -1


def my_search(in_list, x):
    if len(in_list) == 0:
        return -1
    x1 = 0
    x2 = len(in_list) - 1

    while x1 <= x2:
        n = (x1 + x2) // 2
        if x == in_list[n]:
            return n
        elif x > in_list[n]:
            x1 = n + 1
        else:
            x2 = n - 1
    return -1


