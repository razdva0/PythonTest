class Shape:
    pass


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius


circle = Circle(10)
print('issubclass', issubclass(Circle, Shape))
print('issubclass', isinstance(circle, Circle))
print('issubclass', isinstance(circle, Shape))
print('issubclass', isinstance(12, int))
print('issubclass', isinstance('hi', str))
print('issubclass', isinstance('hi', float))
print('callable', callable(circle))  # object that defines __call__() is considered callable
print('callable', callable(Circle))
if hasattr(circle, 'radius'):
    print('getattr', getattr(circle, 'radius'))
    setattr(circle, 'radius', 20)
    print('getattr', getattr(circle, 'radius'))
print('dir', dir(circle))
print('circle.__dict__', circle.__dict__)
print('__name__', __name__)
print('type', type(circle))
circle2 = circle
print('id', id(circle), 'id', id(circle2))
print('repr', repr(circle))
