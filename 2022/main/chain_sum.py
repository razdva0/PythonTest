def chain_sum0(number):
    result = number

    def foo(number2=None):
        nonlocal result
        if number2 is None:
            return result
        result += number2
        return foo
    return foo


def chain_sum1(number):
    result = number

    def foo(number2=None):
        nonlocal result
        try:
            result += number2
            return foo
        except:
            return result
    return foo


def chain_sum3(number):
    def foo(number2=None):
        def inner():
            foo.result += number2
            return foo
        logic = {type(None): lambda: foo.result,
                 int: inner}
        return logic[type(number2)]()
    foo.result = number
    return foo


class chain_sum5:
    def __init__(self, number):
        self._number = number

    def __call__(self, value=0):
        return chain_sum(self._number + value)

    def __str__(self):
        return str(self._number)


class chain_sum(int):
    def __call__(self, value=0):
        return chain_sum(self + value)


print(chain_sum(5))
print(chain_sum(5)(2))
print(chain_sum(5)(100)(-10))