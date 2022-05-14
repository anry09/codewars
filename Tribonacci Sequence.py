def tribonacci(s, n):
    ls = s
    if n == 0:
        return []
    elif n == 1:
        return [s[0]]
    
    elif n == 2:
        return s[0:2]
    elif n == 3:
        return s[0:3]
    count_from = 0
    count_to = 3
    while len(ls) != n:
        ls.append(sum(ls[count_from:count_to]))
        count_from+=1
        count_to+=1
    return ls