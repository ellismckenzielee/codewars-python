#Maze runner kata
#https://www.codewars.com/kata/58663693b359c4a6560001d6

def maze_runner(maze, directions):
    limit = len(maze)
    start_position = [item for row in maze for item in row].index(2)   
    position = [start_position // limit, start_position % limit]
    for direction in directions:
        print(position)
        print(direction)
        if direction == 'N':
            print('N')
            position[0] -= 1
        elif direction == 'E':
            print('E')
            position[1] += 1
        elif direction == 'S':
            print('S')
            position[0] += 1
        elif direction == 'W':
            print('W')
            position[1] -= 1
        check_limits = list(filter(lambda coord: coord >= 0 and coord < limit, position))
        if len(check_limits) != 2 or maze[position[0]][position[1]] == 1:
            return 'Dead'
        elif maze[position[0]][position[1]] == 3:
            return 'Finish'
    return 'Lost'
        