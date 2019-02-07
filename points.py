def points(games):
    '''Count the number of points achieved in a season based on individual game scores'''
    points = 0
    for game in games:
        result = int(game[0]) - int(game[2])
        if result > 0:
            points = points + 3
        elif result == 0:
            points = points + 1
            
    return points