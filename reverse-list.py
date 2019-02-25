def reverse_list(l):
  '''Returns a list with the reverse order of l'''
  return [l[-x] for x in range(1, len(l)+1)]