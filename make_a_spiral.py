#make a spiral kata
#https://www.codewars.com/kata/534e01fbbb17187c7e0000c6

def check_wall(head, direction, background, size):
    '''Checks whether a turn needs to be made based 
    on what is in front in the current direction. Returns 
    true if a change in direction is necessary.'''
    ant = head.copy()
    if direction == 'E':
        ant = [head[0], head[1] + 2]
    if direction == 'W':
        ant = [head[0], head[1] - 2]
    if direction == 'N':
        ant = [head[0] - 2, head[1]]
    if direction == 'S':
        ant = [head[0] + 2, head[1]]
    print(head, ant)
    if size + 2 in ant or -1 in ant:
        print(True)
        return True
    elif background[ant[0]][ant[1]] == 1:
        return True
    
    
        
def move(head, direction):
    '''Increments the head location'''
    if direction == 'E':
        head[1] += 1
    if direction == 'W':
        head[1] -= 1
    if direction == 'N':
        head[0] -= 1
    if direction == 'S':
        head[0] += 1
    return head
        
def spiralize(size):
    background = [[0 for j in range(size + 2)] for i in range(size + 2)]
    head = [1,1]
    directions = ['E', 'S', 'W', 'N']
    direction = directions[0]
    moved_in_direction = 0 
    while True:
        background[head[0]][head[1]] = 1
        change_direction = check_wall(head, direction, background, size)
        if change_direction:
            direction = directions[(directions.index(direction) + 1) % len(directions)]
            
            #Two conditions that mean the spiral has reached as far as possible
            if moved_in_direction == 1:
                break
            if check_wall(head, direction, background, size):
                break
            moved_in_direction = 0
        head = move(head, direction)
        moved_in_direction += 1
    
    #Trims parts of background that were initially added
        
    background = background[1:-1]
    for i, row in enumerate(background):
        background[i] = row[1:-1] 
    return background
        