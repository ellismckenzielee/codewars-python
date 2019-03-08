import numpy as np 
def escape(maze):    
    maze_array = []
    length = len(maze[0])
    height = len(maze)
    for maze_string in maze:
        maze_string_split = list(maze_string)
        maze_array.append(maze_string_split)
    
    maze_array = np.array(maze_array)
    if '^' in maze_array:
        position = np.where(maze_array == '^') 
        starting_direction = 'UP'
    elif '<' in maze_array:
        position = np.where(maze_array == '<') 
        starting_direction = 'LEFT'
    elif '>' in maze_array:
        position = np.where(maze_array == '>') 
        starting_direction = 'RIGHT'
    
    maze_array[maze_array == '#'] = 0
    maze_array[maze_array == ' '] = 1
    maze_array[maze_array == '>'] = 2
    maze_array[maze_array == '<'] = 2
    maze_array[maze_array == '^'] = 2

    for i in range(0,18):
        for (x,y), value in np.ndenumerate(maze_array):
            if (0 < x) and (x < height-1) and (0 < y) and (y < length-1):
                if maze_array[x,y] != 0:
                    centre =  int(maze_array[x,y])
                    t_mid =  int(maze_array[x, y-1])
                    m_left = int(maze_array[x-1, y])
                    m_right = int(maze_array[x+1, y])
                    bot_mid = int(maze_array[x, y+1])
                    total = centre + t_mid + m_left + m_right + bot_mid 
                    if total <= 2:
                        maze_array[x,y] = 0
            
    current_direction = starting_direction

    movements_list = []
    finished = False
    while finished == False:
        potential_position = mover(current_direction, position)
        is_wall_bool = maze_array[potential_position[0], potential_position[1]]
        if int(is_wall_bool[0]) == 0:
            current_direction, rotation = rotate(current_direction, maze_array, position)
            movements_list.append(rotation)
        else:
            movements_list.append('F')
            position = potential_position
        condition1 = int(position[0][0]) == 0
        condition2 = int(position[1][0]) == 0
        condition3 = int(position[0][0]) == maze_array.shape[0]-1
        condition4 = int(position[1][0]) == maze_array.shape[1]-1
      
        if (condition1 or condition2 or condition3 or condition4) != False:
            return movements_list
        else:
            continue 
          
def mover(current_direction, position):
    potential_position = list(position)

    if current_direction == 'RIGHT':
        potential_position[1] = position[1]+1
    elif current_direction == 'LEFT':
        potential_position[1] = position[1]-1
    elif current_direction == 'DOWN':
        potential_position[0] = position[0]+1
    else:
        potential_position[0] = position[0]-1
    
    return potential_position


def rotate(current_direction, maze_array, position):
    lhs = int(maze_array[position[0][0], position[1][0]-1] ) == 0
    above = int(maze_array[position[0][0]-1, position[1][0]]) == 0
    if current_direction == 'UP':
        if lhs == True:
            return 'RIGHT', 'R'
        else:
            return 'LEFT', 'L'
    elif current_direction == 'DOWN':
        if lhs == True:
            return 'RIGHT', 'L'
        else: 
            return 'LEFT', 'R'
    elif current_direction == 'RIGHT':
        if above == True:
            return 'DOWN', 'R'
        else: 
            return 'UP', 'L'
    elif current_direction == 'LEFT':
        if above == True:
            return 'DOWN', 'L'
        else: 
            return 'UP', 'R'




