##The Office V - Find a Chair kata
##https://www.codewars.com/kata/57f6051c3ff02f3b7300008b

def meeting(rooms, need):
    if need == 0:
        return 'Game On'
    taken_chairs = []
    for room in rooms:
        chairs = room[1]
        people = len(room[0])
        chairs_available = chairs - people
        if chairs_available >0:
            if chairs_available >= need:
                taken_chairs.append(need)
                return taken_chairs
            else:
                taken_chairs.append(chairs_available)
                need -= chairs_available
        else:
            taken_chairs.append(0)
    return "Not enough!"