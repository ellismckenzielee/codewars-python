#coordinates validator kata
#https://www.codewars.com/kata/5269452810342858ec000951

def is_valid_coordinates(coordinates):
    ###Check coordinates are actually split
    if ', ' not in coordinates:
        return False
    coord1, coord2 = coordinates.split(', ')
    
    ###Check for incorrect characters
    for char in coord1 + coord2:
        if char not in ['0','1','2','3','4','5','6','7','8','9','.','-','_']:
            print(char)
            return False
    try:
        ###This will be completed if numbers are in the right format (without extra decimals)
        return True if (abs(float(coord1)) <= 90 and abs(float(coord2)) <= 180) else False
    except:
        return False
