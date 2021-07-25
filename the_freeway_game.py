#The Freeway Game
#https://www.codewars.com/kata/59279aea8270cc30080000df

def freeway_game(dist_km_to_exit, my_speed_kph, other_cars):
    my_time = dist_km_to_exit/my_speed_kph
    overtakes = 0
    for car in other_cars:
        speed = car[1] 
        time = car[0]/60
        car_time = dist_km_to_exit/speed + time
        if time < 0:
            if speed >= my_speed_kph:
                pass
            elif speed < my_speed_kph:
                print(True)
                if my_time < car_time:
                    overtakes += 1

        elif time > 0:
            if speed <= my_speed_kph:
                pass
            elif speed > my_speed_kph:
                  if my_time > car_time:
                      overtakes -= 1
                
            
                    
                
    return overtakes          