###Pandemia - codewars kata 
###https://www.codewars.com/kata/5e2596a9ad937f002e510435

def infected(s):
    '''Returns the percentage of infected regions, depending on the geography'''
    islands = s.split('X')
    infected = 0
    safe = 0
    for island in islands:
        if '1' in island:
            infected += len(island)
        else:
            safe += len(island)
    if infected + safe == 0:
        return 0
    return infected/(infected+safe)*100