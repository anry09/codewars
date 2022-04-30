def longest_consec(strarr, k):
    if k > len(strarr) or k <= 0 or len(strarr) == 0:
        return ""
    else:
        s = "".join(strarr[0:k])
        for ind,ele in enumerate(strarr[:len(strarr)-(k-1)]):
            a = "".join(strarr[ind:ind+k])
            if len(a) > len(s): 
                s = a
        return s
            