#Count salutes kata
#https://www.codewars.com/kata/605ae9e1d2be8a0023b494ed

def count_salutes(hallway):
    total = 0
    for i, char in enumerate(hallway):
        if char == '>':
            total += hallway[i:].count('<')
    return total * 2