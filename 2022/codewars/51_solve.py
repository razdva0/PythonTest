def solve(eq: str):
    eq = eq.split('=')
    result = 0
    eq[0] = eq[0].split()
    eq[1] = eq[1].split()
    sym_x = 1
    for x in eq:
        sym = ''
        for s in x:
            if s == '+' or s == '-' or s == 'x':
                if s != 'x':
                    sym = s
                elif s == 'x' and len(sym) > 0:
                    if sym[-1] == '-':
                        sym_x *= -1
                continue
            if 'x' not in x and len(sym) == 0:
                result += int(s)
            elif 'x' in x and len(sym) == 0:
                result -= int(s)
            elif 'x' not in x and sym[-1] == '+' or 'x' in x and sym[-1] == '-':
                result += int(s)
            elif 'x' not in x and sym[-1] == '-' or 'x' in x and sym[-1] == '+':
                result -= int(s)
    return result * sym_x


if solve('x + 1 = 9 - 2') == 6:
    print('OK')
if solve('x - 2 + 3 = 2') == 1:
    print('OK')
if solve('x = + 2 - 5 + 9') == 6:
    print('OK')

if solve('- 10 = x') == -10:
    print('OK')
if solve('- x = - 1') == 1:
    print('OK')
if solve('x - 0 + 0 = 0') == 0:
    print('OK')
if solve('10 + x = 77') == 67:
    print('OK')


def solvex(eq):
    a, b = eq.replace('x', '0').split('=')
    x = eval(a) - eval(b)
    if '- x' in eq:
        x *= -1
    return x if eq.index('x') > eq.index('=') else -x


if solvex('10 + x = 77') == 67:
    print('OK')
