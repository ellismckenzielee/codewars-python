def time_for_milk_and_cookies(dt):
    '''Checks the data, and returns whether Santa needs milk and cookies'''
    date_str = str(dt)
    date_split = date_str.split('-')
    if date_split[1] == '12' and date_split[2] == '24':
        return True
    return False