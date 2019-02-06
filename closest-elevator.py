def elevator(left, right, call):
    '''Return the closest elevator depending on the floor (call). If both are the same, return right'''
    left_distance = abs(call-left)
    right_distance = abs(call-right)
    if right_distance <= left_distance:
        return 'right'
    return 'left'