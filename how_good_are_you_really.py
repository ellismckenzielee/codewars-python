#how good are you really? kata
#https://www.codewars.com/kata/5601409514fc93442500010b

def better_than_average(class_points, your_points):
    return True if your_points > sum(class_points)/len(class_points) else False