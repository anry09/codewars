def alphabet_war(fight):
    left_power = {'w': 4, 'p': 3, 'b': 2, 's': 1}
    right_power = {'m': 4, 'q': 3, 'd': 2, 'z': 1}

    left_score = 0
    right_score = 0

    previous_letter = None
    skip_next = False
    
    for value in fight:
        
        if value == '*':

            if previous_letter in left_power:
                left_score -= left_power[previous_letter]

            if previous_letter in right_power:
                right_score -= right_power[previous_letter]

            skip_next = True
            previous_letter = None
            continue
        if skip_next:
            skip_next = False
            continue

        if value in left_power:
            left_score += left_power[value]

        if value in right_power:
            right_score += right_power[value]
        
        previous_letter = value
    
    if left_score > right_score:
        return "Left side wins!"
    
    if left_score < right_score:
        return "Right side wins!"

    return "Let's fight again!"