import string

def is_pangram(s):
    s=s.upper()
    cha=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    used = []
    c=0
    for i in s:
        if i not in used and i in cha:
            used.append(i)
            c+=1
        else:
            continue
    if c == 26:
        return True
    else:
        return False