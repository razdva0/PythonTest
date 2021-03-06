def sum_array(arr):
    return sum(sorted(arr)[1:-1]) if arr and len(arr) > 1 else 0


assert sum_array([6, 2, 1, 8, 10]) == 16
assert sum_array([6, 0, 1, 10, 10]) == 17
assert sum_array([-6, -20, -1, -10, -12]) == -28
assert sum_array([-6, 20, -1, 10, -12]) == 3