def meeting(s):
    ls = s.upper().split(";")
    ls2 = []
    for i in ls:
        h = i.split(":")
        ls2.append(str(h[1]+", " + h[0]))
    
    ls = ls2
    ls.sort()
    ls3 = []
    for j in ls:
        ls3.append(str("("+j+")"))
    ls = ls3
    return "".join(ls)