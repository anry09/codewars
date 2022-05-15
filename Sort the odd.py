def sort_array(source_array):
    if len(source_array) == 0:
        return []
    else:
        ls = source_array
        indexes = []
        elements = []
        for ind,ele in enumerate(ls):
            if ele % 2 != 0:
                indexes.append(ind)
                elements.append(ele)
        elements.sort()
        zip_ls = zip(indexes,elements)
        for i,e in zip_ls:
            ls[i] = e
        return ls