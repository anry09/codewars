def order_weight(strng):
    # your code
    bar = sorted(strng.split(' '))
    baz = sorted(bar, key=foo)
    return " ".join(baz)
    
    
def foo(n):
    ls = []
    for i in n:
        ls.append(int(i))
    return sum(ls)
