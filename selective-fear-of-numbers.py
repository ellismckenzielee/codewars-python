###Selective fear of numbers - codewars kata
###https://www.codewars.com/kata/55b1fd84a24ad00b32000075

def am_I_afraid(day,num):
    '''Return whether fear is realised based on day and number provided'''
    print(day, num)
    if day == 'Monday':
        return num == 12
    elif day == 'Tuesday':
        return num > 95
    elif day == 'Wednesday':
        return num == 34
    elif day == 'Thursday':
        return num == 0
    elif day == 'Friday':
        return num % 2 == 0
    elif day == 'Saturday':
        return num == 56
    elif day == 'Sunday':
        return (num == 666) == True or (num == -666) == True