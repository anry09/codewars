def solution(number):
    ls = []
    if number < 0 or number == 0:
        ls.append(0)
    else:
        for i in range(1,number):
            if int(i/3) == i/3 or int(i/5) == i/5:
                ls.append(i)
                
            else:
                pass
    return sum(ls)