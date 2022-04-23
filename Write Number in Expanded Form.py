def expanded_form(num):
    ls = []
    for ind,ele in enumerate(str(num)):
        if ele != "0":
            s = "0"*(len(str(num))-(ind+1))
            ls.append(ele+s)
            
        else:
            continue
    return " + ".join(ls)