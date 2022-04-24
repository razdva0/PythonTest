def count_positives_sum_negatives(arr):
    return [len([x for x in arr if x > 0]), sum(x for x in arr if x < 0)] if len(arr) > 0 else []


assert count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]) == [10, -65]
assert count_positives_sum_negatives([0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14]) == [8, -50]
assert count_positives_sum_negatives([1]) == [1, 0]
assert count_positives_sum_negatives([-1]) == [0, -1]
assert count_positives_sum_negatives([0, 0, 0, 0, 0, 0, 0, 0, 0]) == [0, 0]
assert count_positives_sum_negatives([]) == []