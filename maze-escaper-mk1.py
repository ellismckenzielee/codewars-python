import numpy as np

def escape(maze):
    maze_array = []
    for maze_string in maze:
        maze_string_split = list(maze_string)
        maze_array.append(maze_string_split)
    maze_array = np.array(maze_array)
    print(maze_array)
    if '^' in maze_array:
        position = np.where(maze_array == '^' ) 
    elif '<' in maze_array:
        position = np.where(maze_array == '<' ) 
    elif '>' in maze_array:
          position = np.where(maze_array == '>' ) 

    if maze_array[position] == '>':
        starting_direction = 'RIGHT'
    elif maze_array[position] == '<':
        starting_direction = 'LEFT'
    else:
        starting_direction = 'UP'
    
    current_direction = starting_direction
    movements_list = []
    finished = False
    
    while finished == False:
        potential_position = mover(current_direction, position)
        finished = is_complete(position, maze_array)

        if is_wall(potential_position, maze_array) == True:
            current_direction, rotation = rotate(current_direction, maze_array, position)
            movements_list.append(rotation)
        else:
            movements_list.append('F')
            position = potential_position
        finished = is_complete(position, maze_array)
        print(movements_list)
    return movements_list
        
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
    
    
def is_wall(new_position, maze_array):
    try:
        if maze_array[new_position] == '#':
            return True
        else:
            return False
    except:
        return False

def rotate(current_direction, maze_array, position):
    lhs = maze_array[position[0][0]][position[1][0]-1] == '#'
    above = maze_array[position[0][0]-1][position[1][0]] == '#'
    
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
    
def is_complete(position, maze_array):
      condition1 = position[0][0] == 0
      condition2 = position[1][0] == 0
      condition3 = position[0][0] == maze_array.shape[0]
      condition4 = position[1][0] == maze_array.shape[1]
      
      if (condition1 or condition2 or condition3 or condition4) != False:
          return True
      else:
          return False
