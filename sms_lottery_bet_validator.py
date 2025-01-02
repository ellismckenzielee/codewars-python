# SMS lottery bet validator
# https://www.codewars.com/kata/59a3e2897ac7fd05f800005f

import re
def validate_bet(game, text):
    raw_numbers = list(map(int, re.findall(r'[0-9]+(?![;\'\.0-9])', text)))
    numbers = []
    for number in raw_numbers:
        if number in numbers:
            return None
        numbers.append(number)
        
    n, m = game
    if len(numbers) == n and all(map(lambda num: 0 < num <= m, numbers)):
        return sorted(numbers)
