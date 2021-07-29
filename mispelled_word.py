#mispelled word kata
#https://www.codewars.com/kata/5892595f190ca40ad0000095

import difflib
def mispelled(word1,word2):
    if word1 == '' and word2 == '':
        return True
    output_list = [li for li in difflib.ndiff(word2, word1) if li[0] != ' ']
    if len(output_list) <= 2 and (word1 == '' or word2 == ''):
        return False
    return True if len(output_list) <= 2 else False
    