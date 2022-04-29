def mix(s1, s2):
    result = []
    first = dict({x: s1.count(x) for x in s1 if x.islower() and s1.count(x) > 1})
    second = dict({x: s2.count(x) for x in s2 if x.islower() and s2.count(x) > 1})
    final = {key: value for key, value in first.items()}
    for key, value in second.items():
        if key not in final or final[key] < value:
            final[key] = value
    final = dict(reversed(sorted(final.items(), key=lambda items: items[1])))
    if len(final) > 0:
        index = max(final.values())
        tmp = []
        for key, value in final.items():
            if value != index:
                if len(tmp) > 0:
                    result += (sorted(tmp))
                tmp = []
                while value != index:
                    index -= 1
            if value == index:
                if key in first and key in second:
                    if first[key] > second[key]:
                        tmp.append('1:' + key * value)
                    elif first[key] < second[key]:
                        tmp.append('2:' + key * value)
                    else:
                        tmp.append('=:' + key * value)
                elif key in first:
                    tmp.append('1:' + key * value)
                elif key in second:
                    tmp.append('2:' + key * value)
        if len(tmp) > 0:
            result += (sorted(tmp))
    return '/'.join(result)


if mix("Are they here", "yes, they are here") == "2:eeeee/2:yy/=:hh/=:rr":
    print('OK')
# if mix("Sadus:cpms>orqn3zecwGvnznSgacs","MynwdKizfd$lvse+gnbaGydxyXzayp") == '2:yyyy/1:ccc/1:nnn/1:sss/2:ddd/=:aa/=:zz':
#     print('OK')
# if mix("looping is fun but dangerous", "less dangerous than coding") == "1:ooo/1:uuu/2:sss/=:nnn/1:ii/2:aa/2:dd/2:ee/=:gg":
#     print('OK')
# if mix(" In many languages", " there's a pair of functions") == "1:aaa/1:nnn/1:gg/2:ee/2:ff/2:ii/2:oo/2:rr/2:ss/2:tt":
#     print('OK')
# if mix("Lords of the Fallen", "gamekult") == "1:ee/1:ll/1:oo":
#     print('OK')
# if mix("codewars", "codewars") == "":
#     print('OK')
# if mix("A generation must confront the looming ", "codewarrs") == "1:nnnnn/1:ooooo/1:tttt/1:eee/1:gg/1:ii/1:mm/=:rr":
#     print('OK')
