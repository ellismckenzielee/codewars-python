def hero(bullets, dragons):
    '''Checks bullets per dragon and bullet count to see if will survive'''
    return True if dragons == 0 else (bullets/dragons) >= 2