#ticker kata
#https://www.codewars.com/kata/5a959662373c2e761d000183

def ticker(text, width, tick):
    text = ' '*width + text 
    text = list(text)
    output_text = ''
    for num in range(tick, tick+width):
        index = num % len(text)
        output_text += text[index]
    return output_text
