#simple directiosn reversal kata
#https://www.codewars.com/kata/5b94d7eb1d5ed297680000ca

def solve(arr):
    directions, places, output = [], [], []
    for instruction in arr:
        print(instruction)
        direction, place = instruction.split(' on ')
        directions.append(direction)
        places.append(place)
        
    directions[1:] = directions[1:][::-1]
    places = places[::-1]
    
    for i, direction in enumerate(directions):
        if direction == 'Left':
            directions[i] = 'Right'
        elif direction == 'Right':
            directions[i] = 'Left'
        output.append(directions[i] + ' on ' + places[i])
        
    return output  