def rotate(l, n):
    return l[-n:] + l[:-n]
        
    
def who_attack(robot_1, robot_2):
    if robot_1["speed"] == robot_2["speed"]:
        return [robot_1,robot_2]
    
    if robot_1["speed"] > robot_2["speed"]:
        return [robot_1,robot_2]
    
    if robot_1["speed"] < robot_2["speed"]:
        return [robot_2,robot_1]

def who_win(robot_1, robot_2):
    if robot_1["health"] > robot_2["health"]:
        return robot_1["name"] + " has won the fight."

    elif robot_1["health"] < robot_2["health"]:
        return robot_2["name"] + " has won the fight."

    else:
        return  "The fight was a draw."
    
def fight(robot_1, robot_2, tactics):
    robots = who_attack(robot_1, robot_2)
    
    while True:
        a = None
    
        if robots[0]["health"] <= 0 or robots[1]["health"] <= 0:
            break

        if len(robots[0]["tactics"]) == 0 and len(robots[1]["tactics"]) == 0:
            break
        else:
            
            
            if len(robots[0]["tactics"]) > 0:
                a = robots[0]["tactics"].pop(0)
                robots[1]["health"] -= tactics[a]

            robots = rotate(robots, 1)
    
    
    
    
    w = who_win(robot_1, robot_2)
    return w
