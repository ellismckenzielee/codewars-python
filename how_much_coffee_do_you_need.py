#how much coffee do you need? kata
#https://www.codewars.com/kata/57de78848a8b8df8f10005b1

def how_much_coffee(events):
    output = 0
    possible_events = ['cw', 'cat', 'dog', 'movie']
    for event in events:
        if event in possible_events:
            output += 1
        elif event.lower() in possible_events:
            output += 2

    return output if output < 4 else 'You need extra sleep'
        