#Get your steppin' on son kata
#https://www.codewars.com/kata/55e00266d494ce5155000032

def word_step(s):
    words = s.split(' ')
    odds_evens = {'evens': words[0::2],
                  'odds' : words[1::2]}
    x_len = len(''.join(odds_evens['odds'])) - len(odds_evens['odds']) + 1
    y_len = len(''.join(odds_evens['evens'])) - len(odds_evens['evens']) + 1
    arr = [[' ']*y_len for x in range(x_len)]
    direction = 1
    coords = {'x': 0, 'y': 0}
    while odds_evens['odds'] or odds_evens['evens']:
        if direction == 1:
            moving_coord = 'y'
            selector = 'evens'
            
        else:
            moving_coord = 'x'
            selector = 'odds'
        
        word = odds_evens[selector].pop(0)
        
        for l, letter in enumerate(word):
            arr[coords['x']][coords['y']] = letter
            if l != len(word)-1:
                coords[moving_coord] += 1

        
        direction = 1- direction
    return arr