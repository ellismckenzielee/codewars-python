def abbrevName(name):
    '''Return initials of a name in uppercase and with a dot'''
    return str(name.split(' ')[0][0]).upper() + '.' + str(name.split(' ')[1][0]).upper()
    