#turkish numbers 0-99 kata
#https://www.codewars.com/kata/5ebd53ea50d0680031190b96

def get_turkish_number(num):
    print(num)
    singles = [
            'sıfır',
             'bir',
             'iki',
             'üç',
             'dört',
             'beş',
             'altı',
             'yedi',
             'sekiz',
             'dokuz',
            ]
    
    tens = [
            'on',
            'yirmi',
            'otuz',
            'kırk',
            'elli',
            'altmış',
            'yetmiş',
            'seksen',
            'doksan',      
            ]
    
    if num < 10:
        return singles[num % 10]
    elif num % 10 == 0:
        return tens[int(num / 10)-1]
    else:
        return tens[int(num / 10)-1] + ' ' + singles[num % 10]