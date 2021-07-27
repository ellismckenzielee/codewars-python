#fix the pipes kata
#https://www.codewars.com/kata/59f2e89601601434ae000055

import numpy as np
def connect_pipes(pipes,s,e): 
    output = np.zeros((len(pipes),len(pipes[0])), dtype=int)
    print(pipes)
    pipes = np.array([[0] + list(pipe) + [0] for pipe in pipes ])
    row = len(pipes[0])
    s += 1
    e += 1
    pipes[pipes == '.'] = 0
    pipes[pipes == 'x'] = 1
    pipes = pipes.astype(int)
    pipes = np.insert(pipes, [0], np.zeros(len(pipes[0])), axis=0)   
    pipes = np.insert(pipes, len(pipes), np.zeros(len(pipes[0])), axis=0)   
    current_direction = 'R'
    pipes[s][0], pipes[e][row-1] = 1, 1
    pos, counter = [s, 1], 0
    
    while pos != [e, len(pipes[0])-1]:
        shape = [pipes[pos[0]-1][pos[1]], pipes[pos[0]][pos[1]+1], pipes[pos[0]+1][pos[1]], pipes[pos[0]][pos[1]-1]]
        if 1 in [shape[0], shape[2]]:
            if shape in [[0,1,1,0], [0,1,1,1]] and current_direction =='U':
                current_direction = 'R'
                output[pos[0]-1][pos[1]-1] = 9487
                pos[1] = pos[1] + 1
            elif shape in [[0,1,1,1],[0,0,1,1]] and current_direction == 'R':
                current_direction = 'D'
                output[pos[0]-1][pos[1]-1] = 9491
                pos[0] = pos[0] + 1

            elif shape in [[1,1,0,0], [1,1,0,1]] and current_direction == 'D':
                current_direction = 'R'
                output[pos[0]-1][pos[1]-1] = 9495
                pos[1] = pos[1] + 1
             
            elif shape in [[1,0,0,1],[1,1,0,1]] and current_direction == 'R':
                current_direction = 'U'
                output[pos[0]-1][pos[1]-1] = 9499
                pos[0] = pos[0] - 1
            else:
                if current_direction == 'D':
                    output[pos[0]-1][pos[1]-1] = 9475
                    pos[0] = pos[0] + 1
                elif current_direction == 'U':
                    output[pos[0]-1][pos[1]-1] = 9475
                    pos[0] = pos[0] - 1
              
        else:
            output[pos[0]-1][pos[1]-1] = 9473
            pos[1] = pos[1] + 1
            current_direction = 'R'
        if pos == [e, len(pipes[0])-1] :
            break
        
    return output.tolist()