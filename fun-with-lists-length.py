###Fun with lists: length - codewars kata
###https://www.codewars.com/kata/581e476d5f59408553000a4b


def length(head): 
    '''Returns the length of linked list'''
    if head == None:
        return 0
    
    elif head:
        number = 1

        while head.next:
              head = head.next
              number += 1
        return number
                