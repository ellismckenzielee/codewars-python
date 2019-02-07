def whatday(num):
        '''Return day of the week depending on number given'''
    days = {
        1: 'Sunday',
        2: 'Monday',
        3: 'Tuesday',
        4: 'Wednesday',
        5: 'Thursday',
        6: 'Friday',
        7: 'Saturday'}
        
    try:    
        return days[num]
    except:
        return 'Wrong, please enter a number between 1 and 7'
        