def countwords():
    fhand = open('tramp.txt', encoding = 'utf8')
    count = dict()
    most = 0
    for line in fhand:
        line = line.rstrip()
        words = line.split()
        for word in words:
            if word not in count:
                count[word]= 1
            else:
                count[word]=count[word]+1
    lst = list()
    for k,v in count.items():
        lst.append((v,k))
        lst.sort()
    return lst[-1]
print(countwords())
