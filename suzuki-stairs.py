def stairs_in_20(stairs):
    '''Calculates how many stairs suzuki will climb if he climbs 20 per day'''
    total = 0    
    for day in stairs:
        total += sum(day)
    return total*20