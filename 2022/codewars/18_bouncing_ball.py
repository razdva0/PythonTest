def bouncing_ball(h, bounce, window):
    if not 0 < bounce < 1:
        return -1
    rebound = 0
    while h > window:
        rebound += 1
        h *= bounce
        if h > window:
            rebound += 1
    return rebound or -1


if bouncing_ball(2, 0.5, 1) == 1:
    print('OK')
else:
    print(bouncing_ball(2, 0.5, 1))
    print('NO')
if bouncing_ball(3, 0.66, 1.5) == 3:
    print('OK')
else:
    print(bouncing_ball(3, 0.66, 1.5))
    print('NO')
if bouncing_ball(30, 0.66, 1.5) == 15:
    print('OK')
else:
    print(bouncing_ball(30, 0.66, 1.5))
    print('NO')
if bouncing_ball(30, 0.75, 1.5) == 21:
    print('OK')
else:
    print(bouncing_ball(30, 0.75, 1.5))
    print('NO')
