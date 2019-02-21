def areYouPlayingBanjo(name):
    '''Return is playing banjo, if name begins with r or R'''
    if name[0].lower() == 'r':  
        return name + ' plays banjo' 
    else:
        return name + ' does not play banjo'