geese = {"African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"}

def goose_filter(birds):
    '''Return a list of the birds without the geese'''
    return [bird for bird in birds if bird not in geese]