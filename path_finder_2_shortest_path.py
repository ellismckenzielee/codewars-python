#path finder #2: shortest path
#https://www.codewars.com/kata/57658bfa28ed87ecfa00058a

import numpy as np

def check_surrounding(pos, maze, num):
    row, col = pos
    above = [row-1, col]
    below = [row+1, col]
    left = [row, col-1]
    right = [row, col+1]
    dirs = [above, below, left, right]
    for dir in dirs:
        if maze[dir[0],dir[1]] == 0:
            maze[dir[0], dir[1]] = num + 1
    return maze 

        

def scan_matrix(num, maze, dim):
    locations = np.where(maze==num)
    locations = list(zip(locations[0], locations[1]))
    for loc in locations:
        x = loc[0]
        y = loc[1]
        maze = check_surrounding((x,y), maze, num)
    return maze
    
def path_finder(maze):
    maze = np.array(list(map(lambda x: list(x), maze.split('\n'))))
    maze[maze=='.'] = 0
    maze[maze=='W'] = 1
    maze = maze.astype(int)
    dim = maze.shape
    background = np.zeros((dim[0]+2, dim[1]+2))
    background[background == 0.0] = 1
    background[1:-1, 1:-1] = np.copy(maze)
    background = background *-1 
    maze = np.copy(background.astype(int))
    dim = maze.shape
    maze[dim[0]-2, dim[0]-2] = 1
    previous_maze = np.copy(maze)
    cont, counter = True, 1
    while cont == True:
        maze = scan_matrix(counter, np.copy(previous_maze), dim)
        if np.array_equal(previous_maze, maze) or maze[1,1] != 0:
            cont = False
        else:
            previous_maze = np.copy(maze)
            counter += 1
    if maze[1,1] == 0:
        return False
    
    return maze[1,1,] -1 
    