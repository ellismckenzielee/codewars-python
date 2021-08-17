#tetris series #1 - scoring system kata
#https://www.codewars.com/kata/5da9af1142d7910001815d32

import numpy as np
def get_score(arr) -> int:
    points = np.array([40, 100, 300, 1200])
    line_score = 0
    total = 0
    for line in arr:
        if line != 0:
            line_score += line
            total += points[line-1]
        if line_score >= 10:
            points = points + np.array([40, 100, 300, 1200])
            line_score -= 10
    return total
            