def count_squares(cuts):
    '''Count the number of cubes with paint on kata. If a cube is cut in 3 dimensions multiple times
    return the number of cubes which have atleast one red face'''
    return (cuts+1)**(3)-(cuts-1)**3