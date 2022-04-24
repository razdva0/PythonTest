def solution(s):
    return ''.join(x if x.islower() else ' ' + x for x in s)


if solution("helloWorld") == "hello World":
    print('OK')
if solution("camelCase") == "camel Case":
    print('OK')
if solution("breakCamelCase") == "break Camel Case":
    print('OK')
