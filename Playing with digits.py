def dig_pow(n, p):
    ls_numbers = []
    ls_powers = []
    for i in str(n):
        ls_numbers.append(int(i))
        
    for j in range(len(str(n))):
        ls_powers.append(ls_numbers[j]**(p+j))
        
    s = sum(ls_powers)
    d = s/n
    if int(d) == d:
        return d
    else:
        return -1