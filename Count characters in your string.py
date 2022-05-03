def count(string):
    if len(string) == 0:
        return {}
    else:
        d={}
        for ind,ele in enumerate(string):
            if ele not in d.keys():
                d.update({ele:string.count(ele)})
            else:
                pass
        return d