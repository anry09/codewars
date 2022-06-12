def getKey(dct,value):
     return [key for key in dct if (dct[key] == value)]
def most_money(students):
    money = {}
    for i in students:
        h = i.fives*5+i.tens*10+i.twenties*20
        money.update({i.name:h})
    v = list(money.values())
    if v.count(max(v)) == len(v) and len(v)>1:
        return 'all'
    elif len(v) == 1:
        return list(money.keys())[0]
    else:
        return getKey(money,max(v))[0]
