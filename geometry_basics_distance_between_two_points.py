# Geometry Basics: Distance Between Two Points in 2D kata
# https://www.codewars.com/kata/58dced7b702b805b200000be/train/python

import math
def distance_between_points(a, b):
    return math.sqrt((b.y-a.y)**2 + (b.x -a.x)**2)
