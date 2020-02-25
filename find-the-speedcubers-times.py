###Find the speecuber's times - codewars kata
###https://www.codewars.com/kata/5d7c7697e8ad48001e642964/python

def cube_times(times):
    '''Returns the average of the three middle times and the fastest time'''
    times = sorted(times)
    return (round(sum(times[1:4])/3,2), times[0])