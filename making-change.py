###Making Change - codewars kata 
###Return the coins which makes up the change that achieves the minimum number of coins

def make_change(amount):
    '''Returns a dictionary of minimum coins required to reach amount'''
    coins = [50, 25, 10, 5, 1]
    names = ['H','Q','D','N','P']
    output = {}
    for i, coin in enumerate(coins):
        if amount // coin > 0:
            output[names[i]] = amount // coin
        amount %= coin
    return output