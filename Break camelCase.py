def solution(s):
    new_s = []
    for i in s:
        if i.isupper():
            new_s.append(" ")
            new_s.append(i)
        else:
            new_s.append(i)
            
    return "".join(new_s)