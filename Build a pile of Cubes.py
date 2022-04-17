def find_nb( m):
       
    s = 1
    ind = 1
    while s < m:
        ind += 1
        s += ind**3
        
    if s == m:
        return ind
    else:
        return -1