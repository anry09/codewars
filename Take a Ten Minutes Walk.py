def is_valid_walk(walk):
    #North = північ = n
    #South = південь = s
    #West = захід = w
    #East = схід = e
    x = 0
    y = 0
    for i in walk:
        if i == "n":
            y+=1
            
        elif i == "s":
            y-=1
        elif i == "w":
            x-=1
        elif i == "e":
            x+=1
    if x == 0 and y == 0 and len(walk) == 10:
        return True
    
    else:
        return False

print(is_valid_walk(['n','s','n','s','n','s','n','s','n','s']))