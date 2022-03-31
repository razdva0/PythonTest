def land_perimeter(arr):
    result = 0
    i = 0
    while i < len(arr):
        j = 0
        while j < len(arr[i]):
            if arr[i][j] == 'X':
                if i - 1 < 0:
                    result += 1
                elif arr[i - 1][j] == 'O':
                    result += 1
                if i + 1 > len(arr) - 1:
                    result += 1
                elif arr[i + 1][j] == 'O':
                    result += 1
                if j - 1 < 0:
                    result += 1
                elif arr[i][j - 1] == 'O':
                    result += 1
                if j + 1 > len(arr[i]) - 1:
                    result += 1
                elif arr[i][j + 1] == 'O':
                    result += 1
            j += 1
        i += 1
    return f'Total land perimeter: {result}'


if land_perimeter(["OXOOOX", "OXOXOO", "XXOOOX", "OXXXOO", "OOXOOX", "OXOOOO", "OOXOOX", "OOXOOO", "OXOOOO",
                   "OXOOXX"]) == "Total land perimeter: 60":
    print('OK')
if land_perimeter(["OXOOO", "OOXXX", "OXXOO", "XOOOO", "XOOOO", "XXXOO", "XOXOO", "OOOXO", "OXOOX", "XOOOO",
                   "OOOXO"]) == "Total land perimeter: 52":
    print('OK')
if land_perimeter(["XXXXXOOO", "OOXOOOOO", "OOOOOOXO", "XXXOOOXO", "OXOXXOOX"]) == "Total land perimeter: 40":
    print('OK')
if land_perimeter(
        ["XOOOXOO", "OXOOOOO", "XOXOXOO", "OXOXXOO", "OOOOOXX", "OOOXOXX", "XXXXOXO"]) == "Total land perimeter: 54":
    print('OK')
if land_perimeter(["OOOOXO", "XOXOOX", "XXOXOX", "XOXOOO", "OOOOOO", "OOOXOO", "OOXXOO"]) == "Total land perimeter: 40":
    print('OK')
