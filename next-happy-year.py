###See You Next Happy Year - codewars kata
###https://www.codewars.com/kata/5ae7e3f068e6445bc8000046

def next_happy_year(year):
    '''Returns the next year after 'year' in which each digit is unique'''
    happy_year = False
    while happy_year == False:
        year += 1
        if len(set(list(str(year)))) == 4:
            happy_year = True
        
    return year