#leaderboard climbers kata
#https://www.codewars.com/kata/5f6d120d40b1c900327b7e22

def leaderboard_sort(leaderboard, changes):
    for change in changes:
        #Obtain the name and the new index from the current index and the change
        name, change = change.split(' ')
        amount = int(''.join(list(map(lambda x: x if x.isnumeric() else '', change))))
        if '+' in change:
            direction = '+'
        else:
            direction = '-'
            
        if direction == '+':
            new_index = leaderboard.index(name) - amount
        else: 
            new_index = leaderboard.index(name) + amount
     
        #Remove name and then insert at new index
        leaderboard.pop(leaderboard.index(name))
        leaderboard.insert(new_index, name)
    return leaderboard
