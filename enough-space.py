def enough(cap, on, wait):
    '''Return whether or not there will be enough space on a bus'''
    return 0 if on+wait <= cap else (wait+on-cap)