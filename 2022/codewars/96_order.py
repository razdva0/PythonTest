def order(sentence):
    numbers = sorted([x for x in sentence if x.isdigit()])
    result = []
    for x in numbers:
        for z in sentence.split():
            if x in z:
                result.append(z)
    return ' '.join(result)


if order("is2 Thi1s T4est 3a") == "Thi1s is2 3a T4est":
    print('OK')
else:
    print(order("is2 Thi1s T4est 3a"))
if order("4of Fo1r pe6ople g3ood th5e the2") == "Fo1r the2 g3ood 4of th5e pe6ople":
    print('OK')
else:
    print(order("4of Fo1r pe6ople g3ood th5e the2"))
if order("") == "":
    print('OK')
else:
    print(order(""))
