# Quadrants 2: Segments kata
# https://www.codewars.com/kata/643ea1adef815316e5389d17/train/python

def quadrant_segment(A, B): 
    x = A.x > 0 and B.x > 0 or A.x < 0 and B.x < 0
    y = A.y > 0 and B.y > 0 or A.y < 0 and B.y < 0
    return not (x and y)
