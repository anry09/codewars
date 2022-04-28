def find_even_index(arr):
    a = []
    for ind,ele in enumerate(arr):
        if sum(arr[0:ind]) == sum(arr[ind+1:len(arr)]):
            a.append(ind)
            
        
        else:
            continue
    if len(a) == 0:
        return -1
    else:
        return a[0]