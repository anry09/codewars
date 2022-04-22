def order(sentence):
    if len(sentence) == 0:
        return ""
    else:
        words = sentence.split()
        
        a = 10
        ls = words[:]
        s = ["1","2","3","4","5","6","7","8","9",]
        for j in words:
            for i in j:
                if i in s:
                    ls.insert(int(i)-1, j)
                    del ls[int(i)]
        return " ".join(ls)