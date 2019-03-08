def who_is_paying(name):
    '''Returns who will pay for the wall based on length of the name'''
      return [name] if len(name) <= 2 else [name, name[0:2]]