#Move 10 kata
#https://www.codewars.com/kata/57cf50a7eca2603de0000090

def move_ten(st):
    return ''.join(list(map(lambda x: chr(((ord(x)-87)%26)+97), st)))