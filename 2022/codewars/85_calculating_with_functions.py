def zero(s='', n=0): return n if s == '' else eval(str(n) + s)
def one(s='', n=1): return n if s == '' else eval(str(n) + s)
def two(s='', n=2): return n if s == '' else eval(str(n) + s)
def three(s='', n=3): return n if s == '' else eval(str(n) + s)
def four(s='', n=4): return n if s == '' else eval(str(n) + s)
def five(s='', n=5): return n if s == '' else eval(str(n) + s)
def six(s='', n=6): return n if s == '' else eval(str(n) + s)
def seven(s='', n=7): return n if s == '' else eval(str(n) + s)
def eight(s='', n=8): return n if s == '' else eval(str(n) + s)
def nine(s='', n=9): return n if s == '' else eval(str(n) + s)
def plus(n): return '+' + str(n)
def minus(n): return '-' + str(n)
def times(n): return '*' + str(n)
def divided_by(n): return '//' + str(n)


if seven(times(five())) == 35: print('OK')
else: print(seven(times(five())))
if four(plus(nine())) == 13: print('OK')
else: print(four(plus(nine())))
if eight(minus(three())) == 5: print('OK')
else: print(eight(minus(three())))
if six(divided_by(two())) == 3: print('OK')
else: print(six(divided_by(two())))