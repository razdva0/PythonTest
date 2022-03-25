def tribonacci(signature, n):
    lst = []
    i = 0
    j = 0
    while n > len(lst):
        if len(lst) < len(signature):
            lst.append(signature[i])
        else:
            i = j
            n1 = 0
            for x in signature:
                n1 += lst[i]
                i += 1
            lst.append(n1)
            j += 1
        i += 1
    return lst


print(tribonacci([1, 1, 1], 10))


def tribonaccix(signature, n):
    while len(signature) < n:
        signature.append(sum(signature[-3:]))

    return signature[:n]


def tribonaccixx(signature, n):
    output = signature[:n]
    while len(output) < n:
        output.append(sum(output[-3:]))
    return output
