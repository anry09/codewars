def after(l,ind):
    if ind + 13 > len(l) - 1:
        return l[13 - (len(l)-ind)]
    else:
        return l[ind+13]

def rot13(message):
    l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    new_s=[]
    for ind,ele in enumerate(message):
        if ele.lower() in l:
            if ele.isupper():
                h = ele.lower()
                b=l.index(h)
                res = after(l,b)
                new_s.append(res.upper())
            else:
                b=l.index(ele)
                res = after(l,b)
                new_s.append(res)
        else:
            new_s.append(ele)
    return "".join(new_s)