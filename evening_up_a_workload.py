#evening up a workload kata
#https://www.codewars.com/kata/56431c04ed1454a35d00003b

def split_workload(workload):
    if workload == []:
        return (None, None)
    difference = [abs(sum(workload[i:])-sum(workload[0:i])) for i in range(0,len(workload))]
    location = difference.index(min(difference))
    return (location, difference[location])