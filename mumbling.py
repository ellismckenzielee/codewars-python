def accum(s):
    '''accum("abcd") -> "A-Bb-Ccc-Dddd"
        accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
        accum("cwAt") -> "C-Ww-Aaa-Tttt"'''
    output = []
    for count, letter in enumerate(s):
        output.append(letter.upper() + letter.lower()*(count))
    return '-'.join(output)