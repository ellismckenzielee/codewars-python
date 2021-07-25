#Roman numercals decoder kata
#https://www.codewars.com/kata/51b6249c4612257ac0000005

def solution(roman):
    total = 0
    roman = list(roman)[::-1]
    dict = {'I': 1, 'V': 5, 'X': 10,  'L': 50, 'C':100, 'D': 500, 'M': 1000}
    previous_value = 0
    for letter in roman:
        if dict[letter] < previous_value:
            total -= dict[letter]
            previous_value = dict[letter]
        else:            
            total += dict[letter]
            previous_value = dict[letter]
    return total 