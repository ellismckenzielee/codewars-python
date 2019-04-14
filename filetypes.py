def solve(files):
    '''Find the most commonly used file extension from a list of string data'''
    filetype_count = {}
    for song in files:
        song_filetype = song.split('.')[-1]
        song_filetype = '.' + song_filetype
        if song_filetype in filetype_count.keys():
            filetype_count[song_filetype] += 1
        else:
            filetype_count[song_filetype] = 1
    if filetype_count == {}:
        return []
    max_number = 0
    output_list = []
    for key, value in filetype_count.items():
        if value > max_number:
            output_list = [key]
            max_number = value
        elif value == max_number:
            output_list.append(key)
            
    return sorted(output_list)