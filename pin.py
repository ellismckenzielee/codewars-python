def get_pins(observed):
     diction = {'1': [1, 2, 4, 3],
            '2': [1, 2, 3, 5, 4],
            '3': [2, 3, 6, 3],
            '4': [1, 4, 5, 7, 3],
            '5': [2, 4, 5, 6, 8, 5],
            '6': [3, 5, 6, 9, 4],
            '7': [4, 7, 8, 3],
            '8': [5, 7, 8, 9, 0, 5],
            '9': [6, 8, 9, 3],
            '0': [8, 0, 2]}
    
     numbers = list(observed)
     print(numbers)
     possible_numbers = set()
     controller_min = []
     controller_max = []
     for num in numbers:
         controller_min.append(1)
         controller_max.append(diction[num][-1])

     counter = 1
     print(controller_max)
     for i in range(0, len(controller_max)):
          while controller_max[-i] > 0:
               print()

x = get_pins('11')
