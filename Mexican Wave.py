def wave(people):
    ls = []
    for ind, ele in enumerate(people):
        if ele != " ":
            ls.append(people[:ind]+people[ind].upper()+people[ind+1:len(people)])
        else:
            continue
        
    return ls