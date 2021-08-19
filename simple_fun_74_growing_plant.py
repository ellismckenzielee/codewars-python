#simple fun #74: growing plant kata
#https://www.codewars.com/kata/58941fec8afa3618c9000184

import math
def growing_plant(upSpeed, downSpeed, desiredHeight):
    total_height = 0
    counter = 1
    days = 1
    
    while total_height < desiredHeight:
        if counter == 1:
            total_height += upSpeed
            counter = 2
        else:
            total_height -= downSpeed
            counter = 1
            
        days += 1
    
    return math.ceil(days /2)