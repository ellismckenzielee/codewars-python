##FOOTBALL - YELLOW AND RED CARDS KATA
##Code finds the number of players playing at the end of a football match
##Based on the type of card and receiving player
##Game is abandoned if any team has fewer than 7 players remaining

def men_still_standing(cards):
    yellow_cards = set()
    red_cards = set()
    red_card_count = {
        'A': 0,
        'B': 0
        }
        
    for num in cards:
        if 5 in (red_card_count['A'], red_card_count['B']):
            break
        player = num[:-1]
        card = num[-1]
        if card == 'R':
            if player not in red_cards:
                red_card_count[num[0]] += 1
                red_cards.add(player)
        elif card == 'Y':
            if player in yellow_cards and player not in red_cards:
                red_card_count[num[0]] +=1
                red_cards.add(player)
            else:
                yellow_cards.add(player)
    return 11 - red_card_count['A'], 11 - red_card_count['B']