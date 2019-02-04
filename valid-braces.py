def validBraces(string):
    '''Functions takes a string of braces and determines if the order is valid'''
    bracket_l = {'[': 0, '{': 1, '(': 2}
    tracker = []
    
    for bracket in string:
        if bracket in '[{(':
            tracker.append(bracket_l[bracket])
        
        elif len(tracker) > 0:
            if bracket == ']':
                if tracker[-1] == bracket_l['[']:
                    tracker.pop()
                else:
                    return False
                
            elif bracket == '}':
                if tracker[-1] == bracket_l['{']:
                    tracker.pop()
                
                else:
                    return False
            
            elif bracket == ')':
                if tracker[-1] == bracket_l['(']:
                    tracker.pop()
                else:
                    return False
        elif len(tracker) < 0:
            return False
    if tracker:
        return False
    else:
        return True