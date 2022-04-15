def count_smileys(arr):
    eys = [":",";"]
    nose = ["-","~"]
    smile = ["D",")"]
    count = 0
    if len(arr) == 0:
        return 0
    else:
        for i in arr:
            if len(i) == 2:
                if i[0] in eys and i[1] in smile:
                    count += 1
                else:
                    count += 0
            elif len(i) == 3:
                if i[0] in eys and i[1] in nose and i[2] in smile:
                    count += 1
                else:
                    count += 0
            else:
                count += 0
        return count