from math import pi
from functools import reduce

def calculate_volume(object):
    return None


class Shape(object):

    def __init__(self):
        self.subtract = [];

    def volume(self):
        raise Exception('Implement me')

    def childrenVolume(self):
        if len(self.subtract) == 0:
            return 0
        return reduce((lambda x, y: x + y), map((lambda x: x.volume() ), self.subtract))

class Cube(Shape):

    def __init__(self, x, y, z):        
        super(Cube, self).__init__()    
        self.x = x
        self.y = y
        self.z = z

    def volume(self):
        return (self.x * self.y * self.z) - self.childrenVolume()

class Cylinder(Shape):
    # V = Pi * r^2 * h
    def __init__(self, r, h):        
        super(Cylinder, self).__init__()  
        self.r = r
        self.h = h

    def volume(self):
        return (pi * (self.r ** 2) * self.h) - self.childrenVolume()

class Cone(Shape):
    # V= 1/3 * pi * r^2 * h
    def __init__(self, r, h):        
        super(Cone, self).__init__()  
        self.r = r
        self.h = h
    def volume(self):
        return ((pi * (self.r ** 2) * self.h) / 3) - self.childrenVolume()
