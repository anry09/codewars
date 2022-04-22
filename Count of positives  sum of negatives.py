def count_positives_sum_negatives(arr):
    ls = [0,0]
    if len(arr) == 0:
        return []
    else:
        for i in arr:
            if i > 0:
                ls[0]+=1
            elif i < 0:
                ls[1]+=i
            elif i == 0:
                ls[0]+=0
    return ls