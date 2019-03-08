import numpy as np
from itertools import chain

def snail(array):
    '''In an nxn square, a snail moves clockwise around the perimeter and towards the centre,
       this code returns the numbers of each square it slides over, in order'''
      if array[0] == [1]:
            return [1]
      array = np.array(array)
      min_num = 0
      max_num = array.shape[0]-1
      counter = 0
      output = []
      while counter < max_num*10:
          if counter % 2 == 1:
              min_num += 1
              max_num -=1
          array, arr_slice = getrow(array, min_num, 1)
          output.append(arr_slice)
          array,arr_slice = getcolumn(array, max_num, 1)
          output.append(arr_slice)

          array, arr_slice = getrow(array, max_num, 2)
          output.append(arr_slice)

          array, arr_slice = getcolumn(array, min_num, 2)
          output.append(arr_slice)
            
          counter += 1
          if np.sum(array) == 0:
              counter = True
              break
              
      output = list(chain.from_iterable(output))
      output_list = []
      for num in output:
          if num != 0:
              output_list.append(num)
      
      return output_list
      
def getrow(array, rownum, direction):
    row = array[rownum,:]
    new_array = np.copy(array)
    new_array[rownum,:] = 0
    if direction == 2:
        row = row[::-1]
    return new_array, list(row)
    
def getcolumn(array, colnum, direction):
    column = array[:, colnum]
    new_array = np.copy(array)
    new_array[:, colnum] = 0
    if direction == 2:
        column = column[::-1]
    return new_array, list(column)