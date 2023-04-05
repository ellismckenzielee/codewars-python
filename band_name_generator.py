# Band name generator
# https://www.codewars.com/kata/59727ff285281a44e3000011/train/python

def band_name_generator(name):
    if name[0] == name[-1]:
        return name.title() + name[1:]
    return f'The {name.title()}'
