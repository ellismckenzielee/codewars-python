###Which section did you scroll to? - codewars kata
###https://www.codewars.com/kata/5cb05eee03c3ff002153d4ef/train/python

def get_section_id(scroll, sizes):
    '''Returns the size, from sizes (and area on the screen), which has been scrolled to'''
    total_pixels = 0
    for i, num in enumerate(sizes):
        total_pixels += num
        if total_pixels > scroll:
            return i 
    return -1