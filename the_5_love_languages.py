#the 5 love languages kata
#https://www.codewars.com/kata/5aa7a581fd8c06b552000177

def love_language(partner, weeks):
    attempts = weeks * 7
    attempts_split = attempts // 5
    totals = [0,0,0,0,0]
    for i, language in enumerate(LOVE_LANGUAGES):
        for attempt in range(attempts_split):
            response = partner.response(language)
            if response == 'positive':
                totals[i] += 1
            
    return    LOVE_LANGUAGES[totals.index(max(totals))]    