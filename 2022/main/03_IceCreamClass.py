class IceCream:
    def __init__(self, flavor, sprinkles):
        self.flavor = flavor
        self.sprinkles = sprinkles


ice1 = IceCream('Chocolate', 13)
ice2 = IceCream('Vanilla', 0)
ice3 = IceCream('Strawberry', 7)
ice4 = IceCream('Plain', 18)
ice5 = IceCream('ChocolateChip', 3)
menu = {'Plain': 0, 'Vanilla': 5, 'ChocolateChip': 5, 'Strawberry': 10, 'Chocolate': 10}


def sweetest_icecream(lst):
    return max(menu[x.flavor] + x.sprinkles for x in lst)


if sweetest_icecream([ice3, ice1]) == 23:
    print('OK')
