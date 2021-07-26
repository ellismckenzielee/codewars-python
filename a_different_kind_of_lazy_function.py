#A different kind of 'lazy' function kata
#https://www.codewars.com/kata/601d457ce00e9a002ccb7403

import inspect
def lazy(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(inspect.getsource(func), *args)
            if n > 0:
                if decorator.count == n:
                    sol = func(*args, **kwargs)
                else:
                    sol = None
                
                decorator.count -= 1
                
            elif n < 0:
                if decorator.count +1  == 0:
                    sol = None
                else:
                    sol = func(*args, **kwargs)
                decorator.count += 1
                
            if decorator.count  == 0:
                decorator.count = n
            print(n, decorator.count, sol)
            
            return sol
        decorator.count = n
        return wrapper

    return decorator