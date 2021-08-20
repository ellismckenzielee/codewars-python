#mexican wave kata
#https://www.codewars.com/kata/58f5c63f1e26ecda7e000029

def wave(str):
    output_list = []
    for i, letter in enumerate(str):
        if letter.isalpha():
            letter = str[i].upper()
            mexian_wave_string = list(str)
            mexian_wave_string[i] = letter
            output_list.append(''.join(mexian_wave_string))     
    return output_list
        