def nth_fib(n):
    def fibonacci(n):
        a, b = 0, 1
        for _ in range(n):
            yield a
            a, b = b, a + b
    return list(fibonacci(n))[-1]


if nth_fib(1) == 0:
    print('OK')
if nth_fib(2) == 1:
    print('OK')
if nth_fib(3) == 1:
    print('OK')
if nth_fib(4) == 2:
    print('OK')
if nth_fib(5) == 3:
    print('OK')
if nth_fib(6) == 5:
    print('OK')
if nth_fib(7) == 8:
    print('OK')
