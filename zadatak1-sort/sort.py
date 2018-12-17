# zadatak resi ovde

def ref_sort(in_list):
    return sorted(in_list)

def my_sort(in_list):
    if len(in_list) < 2:
        return(in_list)
    else:
        for i in range(len(in_list)):
            n = 1
            while n < len(in_list):
                if in_list[n] < in_list[n-1]:
                    num1 = in_list[n]
                    num2 = in_list[n-1]
                    in_list[n] = num2
                    in_list[n-1] = num1
                n = n + 1
    return in_list
