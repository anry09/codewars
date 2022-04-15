def find_short(s):
    ls = s.split()
    l = 99999999999999999999999999999999999999999
    for i in ls:
        if len(i) <= l:
            l = len(i)
    return l 