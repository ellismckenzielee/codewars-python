#rectangle into rectangles kata
#https://www.codewars.com/kata/58b22dc7a5d5def60300002a

class Rectangle:
  
    def rect_into_rects(lngth, wdth):
        '''Function receives a length and width of rectangle
        and based on the shortest side, iteratively breaks it down
        into smaller and smaller squares. It then returns all the 
        potential rectangles which can be created from these squares'''
        
        print(lngth, wdth)
        
        ###RETURN NONE BASED ON EDGE CONDITIONS
        if (lngth == wdth) or (lngth ==0) or (wdth ==0):
            return None
        
        ###LENGTH ALWAYS SHOULD BE GREATER THAN WIDTH
        if wdth > lngth:
            placeholder = lngth
            lngth = wdth
            wdth = placeholder 
      
        ###ATTACH INITIAL RECTANGLE TO OUTPUT LIST
        output_rectangles = ["("+str(lngth) + "*" + str(wdth) + ")"]

        ###CREATE LIST FOR SIDE LENGTHS AND CUMULATIVE COUNTS AND 
        ###PREVIOUS SHORTEST FOR SPECIAL CASE. (WHEN THE SHORTEST 
        ###SIDE REMAINS THE SHORTEST)
        side_lengths = [lngth, wdth]
        shortest_cumulative_count = 1
        previous_shortest = 0 
        
        
        ###WHILE LOOP FINDS THE SHORTEST SIDE, AND TAKES THE LENGTH
        ###OF THIS AWAY FROM THE LONGEST, CHECKING FOR THE SPECIAL CONDITION
        while side_lengths[0] != side_lengths[1]:
            if side_lengths[0] < side_lengths[1]:
                shortest_index =  0
                longest_index =  1
            else:
                shortest_index = 1
                longest_index = 0
      
        
            shortest = side_lengths[shortest_index]
            longest = side_lengths[longest_index]
            
            ###SPECIAL CONDITION: SHORTEST SIDE REMAINS THE SAME (ADDITIONAL RECTANGLES CAN BE CREATED)
            if ((min(side_lengths) == shortest) and ((side_lengths[longest_index] - shortest) > shortest)):
                shortest_cumulative_count += 1
                previous_longest = longest
                for i in range(2, shortest_cumulative_count+1):
                    print(str(i*shortest), str(shortest))
                    output_rectangles.append("("+str(i*shortest) + "*" + str(shortest) + ")")
            else:
                shortest_cumulative_count = 1
                
            ###REMOVE THE SHORTEST FROM THE LONGEST
            side_lengths[longest_index] -= shortest
            
            ###APPEND THE NEW RECTANGLE SIZE
            if side_lengths[0] < side_lengths[1]:
                output_rectangles.append("("+str(side_lengths[1]) + "*" + str(side_lengths[0]) + ")")
            elif side_lengths[1] < side_lengths[0]:
                print(side_lengths)
                output_rectangles.append("("+str(side_lengths[0]) + "*" + str(side_lengths[1]) + ")")
        
            
        ###RETURN OUTPUT LIST   
        return output_rectangles
        