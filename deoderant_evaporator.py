#deoderant evaporator kata
#https://www.codewars.com/kata/5506b230a11c0aeab3000c1f

import math
def evaporator(content, evap_per_day, threshold):
    return math.ceil(math.log((threshold/100))/math.log((100-evap_per_day)/100))