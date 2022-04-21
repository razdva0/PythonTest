def to_jaden_case(string):
    return ' '.join([x.capitalize() for x in string.split()])


quote = "How can mirrors be real if our eyes aren't real"
if to_jaden_case(quote) == "How Can Mirrors Be Real If Our Eyes Aren't Real":
    print('OK')
else:
    print(to_jaden_case(quote))
