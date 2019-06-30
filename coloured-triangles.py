##COLOURED TRIANGLES KATA
##Given a list of colours are the first row in a triangle,
##return the final colour

def triangle(row):
    if len(row) == 1:
        return row[0]
    new_row = []
    for i in range(0, len(row)-1):
        new_row.append(colour_checker([row[i], row[i+1]]))
    return triangle(new_row)
    
  
def colour_checker(colours):
    if colours[0] == colours[1]:
        print(1)
        return colours[1]
    elif ('B' in colours) and ('G' in colours):
        print(2)
        return 'R'
    elif ('R' in colours) and ('G' in colours):
        return 'B'
    elif ('B' in colours) and ('R' in colours):
        return 'G'