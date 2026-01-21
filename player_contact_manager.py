# Player Contact Manager Solution

def player_manager(players):
    if not players:
        return []
    
    player_contact_dicts = []
    players_info = players.split(", ")
    
    for i in range(0, len(players_info), 2):
        player = players_info[i]
        contact = int(players_info[i+1])
        player_contact_dicts.append(
            {
                "player": player,
                "contact": contact
            }
        )
        
    return player_contact_dicts
