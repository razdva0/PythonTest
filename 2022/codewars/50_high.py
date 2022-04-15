import codewars_test as test


def high(x):
    high_word = 0
    result = ''
    for word in x.split():
        tmp = 0
        for s in word:
            tmp += ord(s) - ord('a') + 1
        if tmp > high_word:
            high_word = tmp
            result = word
    return result


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(high('man i need a taxi up to ubud'), 'taxi')
        test.assert_equals(high('what time are we climbing up the volcano'), 'volcano')
        test.assert_equals(high('take me to semynak'), 'semynak')
        test.assert_equals(high('aa b'), 'aa')
        test.assert_equals(high('b aa'), 'b')
        test.assert_equals(high('bb d'), 'bb')
        test.assert_equals(high('d bb'), 'd')
        test.assert_equals(high("aaa b"), "aaa")
