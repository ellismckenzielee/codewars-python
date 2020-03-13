###Going to the Cinema - codewars kata
###https://www.codewars.com/kata/562f91ff6a8b77dfe900006e

import math
def movie(card, ticket, perc):
    total_card = card 
    total_tickets = 0
    i = 1
    while math.ceil(total_card) >= total_tickets:
        total_card += ticket *(perc**i)
        total_tickets += ticket
        i += 1
    return i - 1
    