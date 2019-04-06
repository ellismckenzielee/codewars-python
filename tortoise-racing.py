import math
def race(v1, v2, g):
    '''Calculates the time required for a tortoise to catch another,
    depending on speed and starting delay'''
    if v2 <= v1:
        return None
    speed_difference = v2 - v1
    time_required = (g/speed_difference)*3600
    hours = int(time_required/3600)
    minutes = int((time_required - hours*3600)/60)
    seconds = int(time_required - hours*3600 - minutes*60)
    return [hours, minutes, seconds]