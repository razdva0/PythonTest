from string import ascii_lowercase as lc, ascii_uppercase as uc


def len_tmp(tmp):
    while len(tmp) % 5 != 0:
        tmp += '1'
    return len(tmp)


def encode_str(strng, shift):
    shift = shift % len(lc)
    if chr(ord(strng[0].lower()) + shift) in lc:
        tmp = strng[0].lower() + chr(ord(strng[0].lower()) + shift)
    else:
        tmp = strng[0].lower() + chr(ord(strng[0].lower()) + shift - len(lc))
    for x in strng:
        if x.isalpha():
            if x.islower() and chr(ord(x) + shift) in lc or x.isupper() and chr(ord(x) + shift) in uc:
                tmp += chr(ord(x) + shift)
            else:
                tmp += chr(ord(x) + shift - len(lc))
        else:
            tmp += x
    result = []
    i = 0
    j = len_tmp(tmp) // 5
    while len(result) < 4:
        result.append(tmp[i:j])
        i = j
        j += len_tmp(tmp) // 5
    if len(tmp[i:]) > 0:
        result.append(tmp[i:])
    return result


def decode(arr):
    arr = ''.join(arr)
    shift = ord(arr[1]) - ord(arr[0])
    result = ''
    for x in arr[2:]:
        if x.isalpha():
            if x.islower() and chr(ord(x) - shift) in lc or x.isupper() and chr(ord(x) - shift) in uc:
                result += chr(ord(x) - shift)
            elif shift > 0:
                result += chr(ord(x) - shift + len(lc))
            else:
                result += chr(ord(x) - shift - len(lc))
        else:
            result += x
    return result


u = "I should have known that you would have a perfect answer for me!!!"
v = ["ijJ tipvme ibw", "f lopxo uibu z", "pv xpvme ibwf ", "b qfsgfdu botx", "fs gps nf!!!"]
if encode_str(u, 1) == v:
    print('OK')
else:
    print(encode_str(u, 1))
v = ['ikK ujqwnf jcx', 'g mpqyp vjcv a', 'qw yqwnf jcxg ', 'c rgthgev cpuy', 'gt hqt og!!!']
if encode_str(u, 28) == v:
    print('OK')
else:
    print(encode_str(u, 28))

u = "abcdefghjuty12"
v = ['abbc', 'defg', 'hikv', 'uz12']
if encode_str(u, 1) == v:
    print('OK')
else:
    print(encode_str(u, 1))
v = ['aeef', 'ghij', 'klny', 'xc12']
if encode_str(u, 30) == v:
    print('OK')
else:
    print(encode_str(u, 30))

u = "O CAPTAIN! my Captain! our fearful trip is done;"
v = ["opP DBQUBJ", "O! nz Dbqu", "bjo! pvs g", "fbsgvm usj", "q jt epof;"]
if decode(v) == u:
    print('OK')
else:
    print(decode(v))
v = ['owW KIXBIQ', 'V! ug Kixb', 'iqv! wcz n', 'miznct bzq', 'x qa lwvm;']
if decode(v) == u:
    print('OK')
else:
    print(decode(v))

u = "NBbofgKvtrvMhwtiEdzdqTynjeFqyvqZxozvFcxgyXwoqd<bas"
v = ['niIWwjabFqo', 'mqHcrodZyuy', 'lOtiezAltql', 'UsjuqAxsbtS', 'rjly<wvn']
if decode(v) == u:
    print('OK')
else:
    print(decode(v))
