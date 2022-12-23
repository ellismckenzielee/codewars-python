# Killer Garage Door kata
# https://www.codewars.com/kata/58b1ae711fcffa34090000ea/python

def controller(events):
    is_moving = False
    direction = "opening"
    directions = ["opening", "closing"]
    current_position = 0
    progress = ''
    for event in events:
        if event == 'P':
            is_moving = not is_moving
            if current_position == 0:
                direction = "opening"
            if current_position == 5:
                direction = "closing"
        if event == "O":
            direction = directions[1 - directions.index(direction)]
        if direction == "opening" and is_moving and current_position < 5:
            current_position += 1
            if current_position == 5:
                is_moving = False
        elif direction == "closing" and is_moving and current_position > 0:
            current_position -= 1
            if current_position == 0:
                is_moving = False
        progress += str(current_position)
    return progress
