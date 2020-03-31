###Generic Algorithm Series - #3 Crossover - codewars kata
###https://www.codewars.com/kata/567d71b93f8a50f461000019/solutions/python

def crossover(chromosome1, chromosome2, index):
    '''Simulates a genetic crossover of chromosomes 1&2 at point index'''
    return [chromosome1[:index] + chromosome2[index:], chromosome2[:index] + chromosome1[index:]]