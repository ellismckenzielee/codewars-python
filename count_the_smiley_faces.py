#Count the smiley faces! kata
#https://www.codewars.com/kata/583203e6eb35d7980400002a

def count_smileys(arr):
    total = 0
    for face in arr:
        template = [[':',';'], ['-','~'], [')','D']]
        if len(face) == 2:
            template = template[0::2]
        elif len(face) != 3:
            continue
        face = list(zip(face, template))
        face = list(map(lambda x: x[0] in x[1], face))
        total += int(all(face))
    return total