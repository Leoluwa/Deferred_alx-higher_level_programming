#!/usr/bin/python3

'''
 This is an example module :)

 This module supplies one function called factorial().
   For instance :

   >>> factorial(5)
   120
'''

def factorial(n):
    '''
     Returns the factorial of n, which
     is an exact integer >= 0 :)

     >>> [factorial(n) for n in range(6)]
     [1, 1, 2, 6, 24, 120]
     >>> factorial(30)
     265252859812191058636308480000000
     >>> factorial(-1)
     Traceback (most recent call last):
         ...
     ValueError: n must be an exact integer
     >>> factorial(30.0)
     265252859812191058636308480000000

     It must also not be ridiculously large:
     >>> factorial(1e100)
     Traceback (most recent call last):
         ...
     OverflowError: n is too large
    '''

    import math
    if not n >= 0:
        raise ValueError('n must be >= 0')
    if math.floor(n) != n:
        raise ValueError('n must be an exact integer')
    if n+1 == n: # Catch a value like 1e300
        raise ValueError('n is too large')
    result = 1
    factor = 2
    while factor <= n:
        result *= factor
        factor += 1
    return result



if __name__ == '__main__':
    import doctest
    doctest.testmod()
