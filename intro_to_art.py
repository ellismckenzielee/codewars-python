#introtoart kata
#https://www.codewars.com/kata/5d7d05d070a6f60015c436d1

def get_w(height):
    if height < 2:
        return []
    width = height*3 + (height-3)
    seeds = [0, int(width/2), int(width/2), width-1]
    w = []
    for i in range(height):
        new_row = [' 'for i in range(width)]
        for i in range(4):
            new_row[seeds[i]] = '*'
            if (i+1) % 2 != 0:
                seeds[i] = seeds[i] + 1
            else:
                seeds[i] = seeds[i] - 1
        w.append(''.join(new_row))
    return w
        