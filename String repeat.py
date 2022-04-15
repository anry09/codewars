def repeat_str(repeat, string):
    s = string
    count = 0
    while count < repeat -1:
        s += string
        count += 1
    return s