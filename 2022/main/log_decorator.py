from functools import wraps  # @wraps(func)


def log_decorator(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        print(f'Calling func {func}')
        func(*args, **kwargs)
        print(f'Func {func} finished its work')
    return wrap


@log_decorator
def hello():
    print("Hello, world!")


hello()
