#!/usr/bin/python3
'''
Defines class called Rectangle :)
'''


class Rectangle:
    ''' A definition of a rectangle based on 3-rectangle.py :) '''
    def __init__(self, width=0, height=0):
        ''' Initializing the rectangle object :) '''
        self.width = width
        self.height = height

    @property
    def width(self):
        ''' getter for private instance attribute called width :) '''
        return self.__width

    @width.setter
    def width(self, value):
        ''' setter for private instance attribute called width :) '''
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        ''' getter for private instance attribute called height :) '''
        return self.__height

    @height.setter
    def height(self, value):
        ''' setter for private instance attribute called height :) '''
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        ''' returns area of the rectangle :) '''
        return(self.__width * self.__height)

    def perimeter(self):
        ''' returns perimater of the rectangle :) '''
        if (self.__width == 0) or (self.__height == 0):
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        ''' returns nicely printable representation of the rectangle :) '''
        string = ''
        if (self.__width != 0) and (self.__height != 0):
            string += '\n'.join('#' * self.__width
                                for j in range(self.__height))
        return string

    def __repr__(self):
        '''
          returns a string representation of the rectangle that
          is suitable for recreating a new instance using eval() :)
        '''
        return ('Rectangle({:d}, {:d})'.format(self.__width, self.__height))

    def __del__(self):
        ''' prints a message when an instance of this class is deleted :) '''
        print('Bye rectangle...')
