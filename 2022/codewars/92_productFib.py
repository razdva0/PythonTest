def productFib(prod):
    first = 0
    second = 1
    while first * second < prod:
        first = first + second
        first, second = second, first
    return [first, second, first * second == prod]


if productFib(4895) == [55, 89, True]:
    print('OK')
if productFib(5895) == [89, 144, False]:
    print('OK')
