def greet(name, owner):
    return 'Hello boss' if name == owner else 'Hello guest'


assert greet('Daniel', 'Daniel') == 'Hello boss'
assert greet('Greg', 'Daniel') == 'Hello guest'
