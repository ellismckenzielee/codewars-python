###Row Weights - codewars kata
###https://www.codewars.com/kata/5abd66a5ccfd1130b30000a9/python

def row_weights(array):
    '''Return the weights each team, according to problem challenge'''
    team1 = array[0::2]
    if len(array) == 1:
        team2 = [0]
    team2 = array[1::2]
    return (sum(team1), sum(team2))