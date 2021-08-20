#baby shark lyrics generator kata
#https://www.codewars.com/kata/5d076515e102162ac0dc514e

def baby_shark_lyrics():
    shks = ['Baby shark', 'Mommy shark', 'Daddy shark', 'Grandma shark', 'Grandpa shark', 'Let\'s go hunt'] 
    output = ''
    for s in shks:
        output += (s + ',' + ' doo'*6 + '\n')*3 + s + '!\n'
    return output + 'Run away,…'
        
            
        