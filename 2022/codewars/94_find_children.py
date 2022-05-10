def find_children(dancing_brigade):
    result = ''
    for x in sorted(dancing_brigade):
        tmp = ''
        if x.isupper():
            tmp += x
            for z in dancing_brigade:
                if ord(z) - 32 == ord(x):
                    tmp += z
        result += tmp
    return result


assert find_children("abBA") == "AaBb"
assert find_children("AaaaaZazzz") == "AaaaaaZzzz"
assert find_children("CbcBcbaA") == "AaBbbCcc"
assert find_children("xXfuUuuF") == "FfUuuuXx"
assert find_children("") == ""
