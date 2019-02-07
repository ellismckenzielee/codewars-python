def sum_pairs(ints, s):
    '''Find the first occurence of two numbers that add to equal s'''
    myset = set()
    for num in ints:
          required = s - num
          if required in myset:
              return [required, num]
          myset.add(num)