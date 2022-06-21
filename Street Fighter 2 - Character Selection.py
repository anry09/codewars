def street_fighter_selection(fighters, initial_position, moves):
    ls = []
    pos = list(initial_position)
    for ind, ele in enumerate(moves):
        
        #"up" comand rule
        if ele == "up":
            if pos[0] == 1:
                pos[0]-=1
                ls.append(fighters[pos[0]][pos[1]])
            elif pos[0]==0:
                pos[0]-=0
                ls.append(fighters[pos[0]][pos[1]])
        
        #"down" comand rule
        elif ele == "down":
            if pos[0] == 0:
                pos[0] += 1
                ls.append(fighters[pos[0]][pos[1]])
            elif pos[0] == 1:
                pos[0]-=0
                ls.append(fighters[pos[0]][pos[1]])
                
        #"right" comand rule
        elif ele == "right":
            pos[1]+=1
            if pos[1]==len(fighters[pos[0]]):
                pos[1]=0
                ls.append(fighters[pos[0]][0])
                
            else:
                ls.append(fighters[pos[0]][pos[1]])
                
        #"left" comand rule    
        elif ele == "left":
            pos[1]-=1
            if pos[1]<0:
                pos[1]=len(fighters[pos[0]])-1
                ls.append(fighters[pos[0]][pos[1]])
            else:
                ls.append(fighters[pos[0]][pos[1]])
    return ls
