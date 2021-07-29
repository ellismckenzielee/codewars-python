#let's recycle! kata
#https://www.codewars.com/kata/5b6db1acb118141f6b000060

def recycle(a):
    bin_indeces = ['paper', 'glass', 'organic', 'plastic']
    bin_contents = ([],[],[],[])
    
    for item in a:
        bin_contents[bin_indeces.index(item['material'])].append(item['type'])
        if 'secondMaterial' in item.keys():
            bin_contents[bin_indeces.index(item['secondMaterial'])].append(item['type'])
    return (bin_contents)