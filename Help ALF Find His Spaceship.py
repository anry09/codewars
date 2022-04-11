def find_spaceship(astromap):
    ls = astromap.split("\n")
    a = []
    for i in ls:
        for j in i:
            if j == "X":
                a.append(i.index("X"))
                a.append((len(ls)-1)-ls.index(i))
                
    if len(a) == 0:
        return 'Spaceship lost forever.'
    else:
        return a