def count_smileys(arr):
    result = 0
    for smile in arr:
        if smile[0] in ':;':
            if len(smile) == 2:
                if smile[1] in ')D':
                    result += 1
            elif len(smile) == 3:
                if smile[1] in '~-' and smile[2] in ')D':
                    result += 1
    return result


if count_smileys([]) == 0:
    print('OK')
if count_smileys([':D',':~)',';~D',':)']) == 4:
    print('OK')
if count_smileys([':)',':(',':D',':O',':;']) == 2:
    print('OK')
if count_smileys([';]', ':[', ';*', ':$', ';-D']) == 1:
    print('OK')


def count_smileysx(arr):
    eyes = [":", ";"]
    noses = ["", "-", "~"]
    mouths = [")", "D"]
    count = 0
    for eye in eyes:
        for nose in noses:
            for mouth in mouths:
                face = eye + nose + mouth
                count += arr.count(face)
    return count
