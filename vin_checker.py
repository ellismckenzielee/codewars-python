#VIN Checker kata
#https://www.codewars.com/kata/60a54750138eac0031eb98e1

def check_vin(number):
    vin = number
    letters = [
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
        'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
        'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
        'Y', 'Z'
              ]
    numbers = [
        1,2,3,4,5,6,7,8,'x',1,2,3,4,5,'x',7,'x',
        9,2,3,4,5,6,7,8,9
    ]
    
    weights = [8,7,6,5,4,3,2,10,0,9,8,7,6,5,4,3,2]

    decoded = []
  
    for char in number:
        char = char.upper()

        if char in letters:
            char = numbers[letters.index(char)]
            if char == 'x':
                return False
                
        decoded.append(int(char))
    
    product = list(map(lambda x: int(x[0] * x[1]), zip(decoded, weights)))
    total = sum(product)
    mod = str(total % 11)
    
    if vin[8] == mod or (mod == '10' and vin[8] == 'X') and len(vin) == 17:
        return True
    return False