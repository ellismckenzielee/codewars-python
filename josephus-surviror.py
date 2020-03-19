###Josephus Survivor - codewars kata
###https://www.codewars.com/kata/555624b601231dc7a400017a

def josephus_survivor(n,k):
    '''Returns the last person standing in a circle of n people, 
    when eliminated in steps of k'''
    n_list = list(range(1,n +1))
    index = (k - 1)
    while len(n_list) > 1:
        while index >= len(n_list):
            index = index - len(n_list)
        del n_list[index % n]
        index += k - 1
    return n_list[0]
        