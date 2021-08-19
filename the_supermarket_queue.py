#the supermarket queue kata
#https://www.codewars.com/kata/57b06f90e298a7b53d000a86

def queue_time(customers, n):
    remaining_customer_list = customers
    tills = [0 for i in range(0, n)]
    
    if len(remaining_customer_list) == 0:
        return 0
        
    elif n >= len(remaining_customer_list):
        return max(customers)
    
    tills[:] = remaining_customer_list[0:len(tills)]
    remaining_customer_list =  remaining_customer_list = remaining_customer_list[len(tills):]
    total_time = 0
    while len(remaining_customer_list) > 0:
        time_to_free_till = min(tills)
        total_time += time_to_free_till
        tills = list(map(lambda x: x - time_to_free_till, tills))
        zero_indeces = [i for i,val in enumerate(tills) if val==0]
        for i, index in enumerate(zero_indeces):
            del tills[index - i]

            
            tills.append(remaining_customer_list[0])
            if len(remaining_customer_list) > 1:
                remaining_customer_list = remaining_customer_list[1:]
            else:
                remaining_customer_list = []
                break
    return total_time + max(tills)    