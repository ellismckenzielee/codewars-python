#counting horses kata
#https://www.codewars.com/kata/5f799eb13e8a260015f58944

def count_horses(sound_str):
    sound_str = list(map(lambda x: int(x), sound_str))
    output = []
    step_size = 1
    while sound_str:
        thumps_in_step = sound_str[step_size-1::step_size]
        if 0 not in thumps_in_step:
            for i in range(step_size-1, len(sound_str), step_size):
                sound_str[i] = sound_str[i] - 1
            output.append(step_size)
        else:
            step_size += 1
        
        if all( [ num == 0  for num in sound_str ]):
            break
    return output