def persistence(n):
    if len(str(n)) ==1:
        return 0
    else:
        count = 0
        c = str(n)
        while len(c)!=1:
            s =1
            for i in c:
                s = s*int(i)
            c = str(s)
            count+=1
        return count
