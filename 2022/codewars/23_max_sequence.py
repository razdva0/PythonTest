def max_sequence(arr):
    result = []
    i = 0
    while i < len(arr):
        tmp = 0
        j = i
        while j < len(arr):
            tmp += arr[j]
            j += 1
            result.append(tmp)
        i += 1
    if len(result) > 0:
        if max(result) > 0:
            return max(result)
    return 0


if max_sequence([]) == 0:
    print('OK')
else:
    print(max_sequence([]))
if max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6:
    print('OK')
else:
    print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))


def maxSequence(arr):
    maximum, curr = 0, 0
    for x in arr:
        curr += x
        if curr < 0:
            curr = 0
        if curr > maximum:
            maximum = curr
    return maximum
