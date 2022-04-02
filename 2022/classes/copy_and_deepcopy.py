import copy

list1 = [1, 2, 3, [4, 5, 6]]

copied_list = list1.copy()
deepcopied_list = copy.deepcopy(list1)
copied_list[3].append(7)
deepcopied_list[3].append(9)
print(list1)
print(copied_list)
print(deepcopied_list)


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point({self.x}, {self.y})'


a = Point(1, 2)
b = copy.copy(a)
a.x = 3
print('a =', a)
print('b =', b)


class Line:

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __copy__(self):
        cls = self.__class__
        result = cls.__new__(cls)
        result.__dict__.update(self.__dict__)
        return result

    def __deepcopy__(self, memodict):
        cls = self.__class__
        result = cls.__new__(cls)
        memodict[id(self)] = result
        for k, v in self.__dict__.items():
            setattr(result, k, copy.deepcopy(v, memodict))
        return result


l1 = Line(a, b)
l2 = copy.copy(l1)
l3 = copy.deepcopy(l1)
l1.p1.x = 4
print('l1 =', l1.p1)
print('l2 =', l2.p1)
print('l3 =', l3.p1)

