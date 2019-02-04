def twice_as_old(dad_years_old, son_years_old):
    '''Calculates how many years ago the father was twice as old as his son, or how many years til he will be'''
    twice_sons_age = 2*son_years_old
    difference = dad_years_old - twice_sons_age
    return abs(difference)