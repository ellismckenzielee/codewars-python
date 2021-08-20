#testing 1-2-3 kata
#https://www.codewars.com/kata/54bf85e3d5b56c7a05000cf9

def number(lines):
    return ['{}: {}'.format(i+1, str(line)) for i, line in enumerate(lines)]