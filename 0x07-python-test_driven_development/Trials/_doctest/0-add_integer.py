#!/usr/bin/python3
'''
 This is the'0-add_integer' module.

 This module supplies one function called add_integer(a, b).
'''


def add_integer(a, b=98):
    '''
     This function takes two int or float arguments
      and returns their integer sum.
    '''
    t_a = type(a)
    t_b = type(b)

    chk_a = (t_a is not int and t_a is not float)
    chk_b = (t_b is not int and t_b is not float)

    if chk_a:
        raise TypeError('a must be an integer')
    if chk_b:
        raise TypeError('b must be an integer')
    if chk_a and chk_b:
        raise TypeError('Both a and b must be integers')

    if t_a is float:
        a = int(a)
    if t_b is float:
        a = int(a)

    return a + b
