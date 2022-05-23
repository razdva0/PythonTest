def controller(func):
    names = []

    def wrap(name):
        nonlocal names
        if name in names:
            print('STOP')
        else:
            names.append(name)
            func(name)
    return wrap


@controller
def hello(name):
    print(f'Hello, {name}')


hello('razdva')
hello('kiyoomi')
hello('razdva')