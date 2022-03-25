def queue_time(customers, n):
    lst = [0] * n
    print(lst)
    for x in customers:
        lst = sorted(lst)
        lst[0] += x
        print(lst)
    return max(lst)


print(queue_time([1, 2, 3], 3))
