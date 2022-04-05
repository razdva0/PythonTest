import itertools


def rolldice_sum_prob(sum_, dice_amount):
    result = [x for x in itertools.product([1, 2, 3, 4, 5, 6], repeat=dice_amount) if sum(x) == sum_]
    return len(result) / 6 ** dice_amount


if rolldice_sum_prob(11, 2) == 0.05555555555555555:
    print('OK')
else:
    print(rolldice_sum_prob(11, 2))
if rolldice_sum_prob(8, 2) == 0.1388888888888889:
    print('OK')
else:
    print(rolldice_sum_prob(8, 2))
if rolldice_sum_prob(8, 3) == 0.09722222222222222:
    print('OK')
else:
    print(rolldice_sum_prob(8, 3))
