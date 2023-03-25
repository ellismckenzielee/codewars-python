# Cats and Shelves kata
# https://www.codewars.com/kata/62c93765cef6f10030dfa92b

# def solution(start, finish):  
#     current_level, jumps = start, 0
#     while current_level < finish:
#         step = 1
#         if finish - current_level >= 3:
#             step = 3
#         current_level += step
#         jumps += 1

#     return jumps

def solution(start, finish):
    steps_of_three = (finish - start) // 3
    steps_of_one =  (finish - start) - steps_of_three*3
    return steps_of_three + steps_of_one
