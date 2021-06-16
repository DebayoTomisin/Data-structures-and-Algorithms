from abc import ABCMeta
from abc import abstractmethod
import  math
print('this is it gentlemen')
""" This is basically me brushing up on my python skills"""

class Shape(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, r=1):
        self.radius = r

    def setRadius(self, r):
        self.radius = r

    def area(self):
        return math.pi * math.pow(self.radius, 2)

    def perimeter(self):
        return 2 * math.pi * self.radius


class HelloWorld(object):
    @classmethod
    def main(cls, args):
        print('Hello World')


if __name__ == '__main__':
    import sys

    HelloWorld.main(sys.argv)


class ParameterPass:
    def __init__(self):
        A = [1, 2]
        self.Change(A)
        print(A)

    def Change(self, G):
        G.append(5)


rit = [1, 4]
tee = rit
tee.append(8)
print(tee)
print(rit)

u = 8
