###Odder Than the Rest - codewars kata
###https://www.codewars.com/kata/5983cba828b2f1fd55000114

def odd_one(arr):
    '''Returns the index of the sole odd value in arr'''
    odds = list(map(lambda x: (x % 2 == 0 and x != 0), arr))
    print(odds)
    if False in odds:
        return odds.index(False)
    return -1