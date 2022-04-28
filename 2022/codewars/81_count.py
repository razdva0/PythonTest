def count(string):
    return {x: string.count(x) for x in string}


from collections import Counter


def countx(string):
    return Counter(string)