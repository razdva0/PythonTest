def content_weight(bottle_weight, scale):
    result = bottle_weight // (int(scale.split()[0]) + 1)
    return result * int(scale.split()[0]) if scale.split()[2] == 'larger' else result


assert content_weight(120, "2 times larger") == 80
assert content_weight(180, "2 times larger") == 120
assert content_weight(500, "9 times larger") == 450
assert content_weight(1000, "49 times larger") == 980
assert content_weight(1000, "999 times larger") == 999

assert content_weight(120, "2 times smaller") == 40
assert content_weight(300, "2 times smaller") == 100
assert content_weight(1000, "4 times smaller") == 200
assert content_weight(1000, "49 times smaller") == 20
assert content_weight(10000, "999 times smaller") == 10
