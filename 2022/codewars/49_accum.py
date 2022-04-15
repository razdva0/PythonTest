import unittest


def accum(s):
    i = 1
    result = []
    for x in s:
        j = 0
        tmp = ''
        while j < i:
            if j == 0:
                tmp += x.upper()
            else:
                tmp += x.lower()
            j += 1
        result.append(tmp)
        i += 1
    return '-'.join(result)
# return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))


class Test(unittest.TestCase):

    def test1(self):
        s = "ZpglnRxqenU"
        result = accum(s)
        self.assertEqual(result, "Z-Pp-Ggg-Llll-Nnnnn-Rrrrrr-Xxxxxxx-Qqqqqqqq-Eeeeeeeee-Nnnnnnnnnn-Uuuuuuuuuuu")

    def test2(self):
        s = "NyffsGeyylB"
        result = accum(s)
        self.assertEqual(result, "N-Yy-Fff-Ffff-Sssss-Gggggg-Eeeeeee-Yyyyyyyy-Yyyyyyyyy-Llllllllll-Bbbbbbbbbbb")

    def test3(self):
        s = "MjtkuBovqrU"
        result = accum(s)
        self.assertEqual(result, "M-Jj-Ttt-Kkkk-Uuuuu-Bbbbbb-Ooooooo-Vvvvvvvv-Qqqqqqqqq-Rrrrrrrrrr-Uuuuuuuuuuu")

    def test4(self):
        s = "EvidjUnokmM"
        result = accum(s)
        self.assertEqual(result, "E-Vv-Iii-Dddd-Jjjjj-Uuuuuu-Nnnnnnn-Oooooooo-Kkkkkkkkk-Mmmmmmmmmm-Mmmmmmmmmmm")

    def test5(self):
        s = "HbideVbxncC"
        result = accum(s)
        self.assertEqual(result, "H-Bb-Iii-Dddd-Eeeee-Vvvvvv-Bbbbbbb-Xxxxxxxx-Nnnnnnnnn-Cccccccccc-Ccccccccccc")


if __name__ == '__main__':
    unittest.main()
